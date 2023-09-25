from django.contrib import admin
from core.models import Person, Attendance, Task, Payment, Project, SalaryInvoice, ProjectInvoice

# Register your models here.

REGISTERED_MODELS = [
    Person, Attendance, Task, Payment, Project, SalaryInvoice, ProjectInvoice
]

admin.site.register(REGISTERED_MODELS)
