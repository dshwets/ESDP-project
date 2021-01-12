from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from employees.models import Employee


class EmployeeDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'employee_delete.html'
    model = Employee
    permission_required = 'employees.can_delete_employee'
    success_url = reverse_lazy('employees:employee_list')
