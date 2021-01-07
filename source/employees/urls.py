from django.urls import path

from employees.views.employee_detail import EmployeeDetailView

app_name = 'employees'

urlpatterns = [
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
]