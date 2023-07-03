from django.contrib import admin
from core.models import Employee, Client, Attendance, Task, Payment, Project, SalaryInvoice, ProjectInvoice

# Register your models here.

REGIDTERED_MODELS = [
    Employee, Client, Attendance, Task, Payment, Project, SalaryInvoice, ProjectInvoice
]

admin.site.register(REGIDTERED_MODELS)
