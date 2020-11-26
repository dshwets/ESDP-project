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
        # TODO поменять url на страницу детального просмотра исполнителя
        return reverse('hostelguests:guest_list')