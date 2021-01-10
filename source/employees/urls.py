from django.urls import path

from employees.views.employee_create import EmployeeCreateView
from employees.views.employee_detail import EmployeeDetailView
from employees.views.employee_list import EmployeeListView

app_name = 'employees'

urlpatterns = [
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/list/', EmployeeListView.as_view(), name='employee_list'),
    path('employee/add/', EmployeeCreateView.as_view(), name='employee_create'),
]