from django.urls import path, include
from core import views

from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings


router = DefaultRouter()
router.register('employees', views.EmployeeView, basename='Employees')
router.register('salary_invoices', views.SalaryInvoiceView, basename='Salary Invoices')
router.register('clients', views.ClientView, basename='Clients')
router.register('attendances', views.AttendanceView, basename='Attendances')
router.register('tasks', views.TaskView, basename='Tasks')
router.register('payments', views.PaymentView, basename='Payments')
router.register('projects', views.ProjectView, basename='Projects')
router.register('project_invoices', views.ProjectInvoiceView, basename='Project Invoices')


urlpatterns = [

    path('', views.index),
    path('api/', include(router.urls)),

    path('api/login/', views.login, name='Login'),

    path('api/get_profile/', views.get_profile, name='Get Profile'),
    path('api/update_profile/', views.update_profile, name='Update Profile'),

    path('api/update_task/<str:pk>/', views.update_task, name='Update Task')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

