from rest_framework import serializers
from core.models import Employee, Client, Attendance, Task, Payment, Project, SalaryInvoice, ProjectInvoice
from django.contrib.auth.models import Group



class EmployeeSerializer(serializers.ModelSerializer):
    employee_username = serializers.StringRelatedField(source='user.username')
    employee_groups = serializers.StringRelatedField(source='user.groups')
    class Meta:
        model = Employee
        fields = '__all__'



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'



class AttendanceSerializer(serializers.ModelSerializer):
    # date_created_gte = serializers.DateTimeField(source='date_created__gte')
    employee_username = serializers.StringRelatedField(source='employee.user.username')
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
    members_username = serializers.StringRelatedField(source='members', many=True, read_only=True)
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