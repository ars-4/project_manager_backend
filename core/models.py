from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class BaseModel(models.Model):
    date_created = models.DateTimeField(default=datetime.now())
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True



class Employee(BaseModel):
    profile_picture = models.ImageField(upload_to='employees/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=244, null=True)
    last_name = models.CharField(max_length=244, null=True)
    email = models.CharField(max_length=244, null=True)
    mobile = models.CharField(max_length=244, null=True)
    address = models.CharField(max_length=244, null=True)
    city = models.CharField(max_length=144, null=True)
    
    salary = models.CharField(max_length=244, null=True)
    designation = models.CharField(max_length=244, null=True)

    def __str__(self):
        return self.first_name



class Attendance(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=144, null=True, choices=(('present', 'present'), ('absent', 'absent'), ('leave', 'leave')))

    def __str__(self):
        return self.employee.user.username



class Client(BaseModel):
    username = models.CharField(max_length=144, null=True)
    first_name = models.CharField(max_length=244, null=True)
    last_name = models.CharField(max_length=244, null=True)
    email = models.CharField(max_length=244, null=244)
    # amount = models.CharField(max_length=244, null=True)

    def __str__(self):
        return self.username



class Project(BaseModel):
    title = models.CharField(max_length=244, null=True)
    description = models.TextField()
    members = models.ManyToManyField(Employee)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    duration_start = models.DateField(null=True)
    duration_end = models.DateField(null=True)
    amount = models.CharField(max_length=244, null=True)

    def __str__(self):
        return self.title



class Task(BaseModel):
    title = models.CharField(max_length=244, null=True)
    description = models.TextField(null=True)
    status = models.CharField(choices=(
        ('pending', 'Pending'),
        ('completed', 'Completed')
    ), null=True, max_length=100)
    assigned_to = models.ManyToManyField(Employee)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    


class ProjectInvoice(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=244, null=True)
    amount = models.CharField(max_length=244, null=True)
    status = models.CharField(max_length=244, null=True, choices=(('due', 'due'), ('paid', 'paid')))

    def __str__(self):
        return self.title
    

class SalaryInvoice(BaseModel):
    person = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=244, null=True)
    amount = models.CharField(max_length=244, null=True)
    status = models.CharField(max_length=244, null=True, choices=(('due', 'due'), ('paid', 'paid')))

    def __str__(self):
        return self.person.user.username
    


class Payment(BaseModel):
    title = models.CharField(max_length=244, null=True)
    description = models.TextField(null=True, default='null')
    type = models.CharField(max_length=244, null=True, choices=(
        ('general', 'general'),
        ('expense', 'expense'),
        ('profit', 'profit')
    ))

    def __str__(self):
        return self.title