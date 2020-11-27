from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import DeleteView
from serviceexecutors.models import ServiceExecutor


class ServiceExecutorDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'serviceexecutor_delete.html'
    model = ServiceExecutor
    permission_required = 'serviceexecutors.can_delete_serviceexecutor'

    def get_success_url(self):
        #TODO поменять редирект на список исполнителей
        return reverse('hostelguests:guest_list')
