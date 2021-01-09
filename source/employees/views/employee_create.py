from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView

from employees.forms import EmployeeForm
from employees.models import Employee


class ServiceExecutorCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'employee_create.html'
    form_class = EmployeeForm
    model = Employee
    permission_required = 'employees.can_add_employee'

    def get_success_url(self):
        return reverse('serviceexecutors:serviceexecutor_view', kwargs={'pk': self.object.pk})