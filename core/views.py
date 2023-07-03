from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from core.utils import get_or_create_token
from core.serializers import EmployeeSerializer, ClientSerializer, AttendanceSerializer, ProjectSerializer, ProjectInvoiceSerializer, SalaryInvoiceSerializer, TaskSerializer, PaymentSerializer
from core.models import Employee, Client, Attendance, Task, Payment, Project, ProjectInvoice, SalaryInvoice
# Create your views here.



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
        if user.check_password(request.data.get('pass')):
            token = get_or_create_token(user)
            status = 200
            data = { 'error':'false', 'msg':'user_log_in_successful', 'token':str(token)}
        else:
            data = {'error': 'true', 'msg': 'wrong_password'}
            status = 403
    except Exception as error:
        data = {'error': 'true', 'msg': str(error)}
        status = 404
    return Response(data, status=status)



@api_view(['GET'])
def get_profile(request):
    employee = Employee.objects.get(user=request.user)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def update_profile(request):
    employee = Employee.objects.get(user=request.user)
    data = request.data
    employee.first_name = data.get('first_name')
    employee.last_name = data.get('last_name')
    employee.email = data.get('email')
    employee.address = data.get('address')
    employee.city = data.get('city')
    employee.save()
    return Response({ 'error':'false', 'msg':'update_success' }, status=203)


class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # employees = Employee.objects.filter(designation='None')
        # return employees
        if self.request.user.username == 'admin':
            # group = Group.objects.get(name='admin')
            # print(self.request.user.groups[0])
            return self.queryset
        else:
            return Response({'error':'true', 'msg':'forbidden'}, status=403)

    def create(self, request):
        post = request.data
        status = 201
        data = {}
        if request.user.username == 'admin':
            try:
                user = User.objects.create_user(
                    username=post['user'], email=post['email'], password=post['pass'],
                    first_name=post['first_name'], last_name=post['last_name']
                    )
                user.save()
                employee = Employee.objects.create(
                    profile_picture='/employees/Black.jpg',
                    user=user, first_name=user.first_name, last_name=user.last_name, email=user.email,
                    mobile=post.get('mobile'), address=post.get('address'), city=post.get('city'),
                    salary=post.get('salary'), designation=post.get('designation')
                )
                employee.save()
                invoice = SalaryInvoice.objects.create(person=employee, title='initial_auto_invoice', amount='0', status='paid')
                invoice.save()
                serializer = EmployeeSerializer(employee, many=False)
                data = {'error':'false', 'msg':'employee_creation_successful', 'data':serializer.data}
                status = 201
            except Exception as error:
                data = {'error':'true', 'msg':str(error)}
                status=403
        
        else:
            data={'error':'true', 'msg':'forbidden'}
            status=403

        return Response(data, status=status)



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
            employee=Employee.objects.get(id=request.data.get('id')),
            status=request.data.get('status')
        )
        attendance.save()
        return Response({
            "error":'false',
            "msg":'attendance_marked'
        }, status=201)



class ClientView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer



class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'



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



class SalaryInvoiceView(ModelViewSet):
    queryset = SalaryInvoice.objects.all()
    serializer_class = SalaryInvoiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

