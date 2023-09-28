from django.contrib import admin
from core.models import Person, Attendance, Task, Payment, Project, SalaryInvoice, ProjectInvoice, Ticket

# Register your models here.

REGISTERED_MODELS = [
    Person, Attendance, Task, Payment, Project, SalaryInvoice, ProjectInvoice, Ticket
]

admin.site.register(REGISTERED_MODELS)
