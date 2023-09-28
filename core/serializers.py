from rest_framework import serializers
from core.models import Person, Attendance, Task, Payment, Project, SalaryInvoice, ProjectInvoice, Ticket
from django.contrib.auth.models import Group



class PersonSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source='user.username')
    groups = serializers.StringRelatedField(source='user.groups')
    class Meta:
        model = Person
        fields = '__all__'



class AttendanceSerializer(serializers.ModelSerializer):
    # date_created_gte = serializers.DateTimeField(source='date_created__gte')
    username = serializers.StringRelatedField(source='employee.user.username')
    class Meta:
        model = Attendance
        fields = '__all__'



class TaskSerializer(serializers.ModelSerializer):
    assignees = serializers.StringRelatedField(source='assigned_to', many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'



class ProjectSerializer(serializers.ModelSerializer):
    employees_username = serializers.StringRelatedField(source='employees', many=True, read_only=True)
    clients_username = serializers.StringRelatedField(source='clients', many=True, read_only=True)
    class Meta:
        model = Project
        fields = '__all__'



class ProjectInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInvoice
        fields = '__all__'


class SalaryInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryInvoice
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'