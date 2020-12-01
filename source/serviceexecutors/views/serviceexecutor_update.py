from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from serviceexecutors.forms import ServiceExecutorForm
from serviceexecutors.models import ServiceExecutor


class ServiceExecutorUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'serviceexecutor_update.html'
    form_class = ServiceExecutorForm
    model = ServiceExecutor
    permission_required = 'serviceexecutors.can_change_serviceexecutor'

    def get_success_url(self):
        return reverse('serviceexecutors:serviceexecutor_view', kwargs={'pk': self.object.pk})