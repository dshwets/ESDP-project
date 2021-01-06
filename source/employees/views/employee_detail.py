from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView
from employees.models import Employee

class EmployeeDetailView(PermissionRequiredMixin, DetailView):
    model = Employee
    template_name = 'employee_detail.html'
    permission_required = 'employees.can_view_employee'