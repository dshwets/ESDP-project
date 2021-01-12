from django.contrib.auth.mixins import  PermissionRequiredMixin
from django.views.generic import ListView

from employees.models import Employee


class EmployeeListView(PermissionRequiredMixin, ListView):
    template_name = 'employee_list.html'
    model = Employee
    context_object_name = 'employees'
    permission_required = 'employees.can_view_employee'
    paginate_by = 20
    paginate_orphans = 4
    ordering = ['-last_name']
