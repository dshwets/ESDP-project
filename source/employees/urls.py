from django.urls import path

from employees.views.employee_create import EmployeeCreateView
from employees.views.employee_detail import EmployeeDetailView
from employees.views.employee_list import EmployeeListView
from employees.views.employee_delete import EmployeeDeleteView

app_name = 'employees'

urlpatterns = [
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/add/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
]