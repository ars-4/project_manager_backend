import json
from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from core.utils import get_or_create_token
from core.serializers import PersonSerializer, AttendanceSerializer, ProjectSerializer, ProjectInvoiceSerializer, SalaryInvoiceSerializer, TaskSerializer, PaymentSerializer, TicketSerializer
from core.models import Person, Attendance, Task, Payment, Project, ProjectInvoice, SalaryInvoice, Ticket
from chats.models import Room



@api_view(['GET'])
def index(request):
    return Response({
        "Message": "Welcome To Manager"
    }, status=502)



@api_view(['POST'])
def login(request):
    status = 200
    data = {}
    try:
        user = User.objects.get(username=request.data.get('user'))
        person = Person.objects.get(user=user)
        if user.check_password(request.data.get('pass')) and person.type == 'employee':
            token = get_or_create_token(user)
            status = 200
            data = { 'error':'false', 'msg':'user_log_in_successful', 'token':str(token), 'data':person.user.username, 'id': person.id}
        elif person.type == 'client':
            return Response({'error': 'true', 'msg': 'no_user'}, status=403)
        else:
            data = {'error': 'true', 'msg': 'wrong_password'}
            status = 403
    except Exception as error:
        data = {'error': 'true', 'msg': str(error)}
        status = 404
    return Response(data, status=status)



@api_view(['GET'])
def get_profile(request):
    employee = Person.objects.get(user=request.user)
    serializer = PersonSerializer(employee, many=False)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def update_profile(request):
    employee = Person.objects.get(user=request.user)
    data = json.loads(request.data['user'])
    employee.first_name = data.get('first_name')
    employee.last_name = data.get('last_name')
    employee.email = data.get('email')
    employee.address = data.get('address')
    employee.city = data.get('city')
    if request.data.get('file') is not None:
        employee.profile_picture = request.data.get('file')
    employee.save()
    return Response({ 'error':'false', 'msg':'update_success' }, status=203)


class EmployeeView(ModelViewSet):
    queryset = Person.objects.filter(type='employee')
    serializer_class = PersonSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Person.objects.filter(type='employee')
        if self.request.user.username == 'admin':
            # group = Group.objects.get(name='admin')
            # print(self.request.user.groups[0])
            return queryset
        else:
            # return Response({'error':'true', 'msg':'forbidden'}, status=403)
            return queryset

    def create(self, request):
        post = request.data
        post = json.loads(post['employee'])
        status = 201
        data = {}
        if self.request.user.username == 'admin':
            try:
                user = User.objects.create_user(
                    username=post['user'], email=post['email'], password=post['pass'],
                    first_name=post['first_name'], last_name=post['last_name']
                    )
                user.save()
                employee = Person.objects.create(
                    profile_picture='/employees/Black.jpg',
                    user=user, first_name=user.first_name, last_name=user.last_name, email=user.email,
                    mobile=post.get('mobile'), address=post.get('address'), city=post.get('city'),
                    salary=post.get('salary'), designation=post.get('designation'), type='employee'
                )
                if request.data.get('picture') is not None:
                    employee.profile_picture = request.data.get('picture')
                employee.save()
                invoice = SalaryInvoice.objects.create(employee=employee, title='initial_auto_invoice', amount='0', status='paid')
                invoice.save()
                serializer = PersonSerializer(employee, many=False)
                data = {'error':'false', 'msg':'employee_creation_successful', 'data':serializer.data}
                status = 201
            except Exception as error:
                data = {'error':'true', 'msg':str(error)}
                status=403
        
        else:
            data={'error':'true', 'msg':'forbidden'}
            status=403

        return Response(data, status=status)
    

class SalaryInvoiceView(ModelViewSet):
    queryset = SalaryInvoice.objects.all()
    serializer_class = SalaryInvoiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def create(self, request):
        data = request.data
        serializer = SalaryInvoiceSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        payment = Payment.objects.create(
            amount=data.get('amount'),
            title='employee_monthly_salary',
            description=data.get('description'),
            type='expense'
        )
        payment.save()
        return Response(serializer.data, status=201)


class AttendanceView(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    ordering_fields = '__all__'
    filterset_fields = {
        'status': ['exact'],
        'employee': ['exact'],
        'date_created': ['exact', 'gte', 'lte'],
    }

    def create(self, request):
        attendance = Attendance.objects.create(
            employee=Person.objects.get(id=request.data.get('id')),
            status=request.data.get('status')
        )
        attendance.save()
        return Response({
            "error":'false',
            "msg":'attendance_marked'
        }, status=201)



class ClientView(ModelViewSet):
    queryset = Person.objects.filter(type='client')
    serializer_class = PersonSerializer



class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def create(self, request):
        data = request.data
        project = Project.objects.create(
            title = data.get('title'),
            description = data.get('description'),
            duration_start = data.get('duration_start'),
            duration_end = data.get('duration_end'),
            amount = data.get('amount'),
        )
        project.employees.set(data.get('employees'))
        project.clients.set(data.get('clients'))
        project.save()
        serializer = ProjectSerializer(project, many=False)
        room = Room.objects.create(
            name = data.get('title'),
            description = data.get('description'),
            project = Project.objects.get(id=serializer.data.get('id')),
            type = 'public',
        )
        room.name = "_".join(room.name.split(" ")).lower()
        for client in data.get('clients'):
            room.members.add(client)
        for employee in data.get('employees'):
            room.members.add(employee)
        room.save()
        return Response(serializer.data, status=201)


class ProjectInvoiceView(ModelViewSet):
    queryset = ProjectInvoice.objects.all()
    serializer_class = ProjectInvoiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def create(self, request):
        data = request.data
        serializer = ProjectInvoiceSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        payment = Payment.objects.create(
            amount=data.get('amount'),
            title='project_invoice',
            description=data.get('description'),
            type='profit'
        )
        payment.save()
        return Response(serializer.data, status=201)



class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


@api_view(['POST'])
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    task.status = request.data.get('status')
    task.save()
    return Response({'error':'false', 'msg':'task_status_updated'}, status=201)



class PaymentView(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class TicketView(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def create(self, request):
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        project = Project.objects.get(id=request.data.get('project'))
        task = Task.objects.create(
            title = request.data.get('title'),
            description = request.data.get('description') or 'null',
            status='pending',
            project=project
        )
        task.assigned_to.set(project.employees.all())
        task.save()
        return Response(serializer.data, status=201)