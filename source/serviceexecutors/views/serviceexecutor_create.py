from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView
from serviceexecutors.forms import ServiceExecutorForm
from serviceexecutors.models import ServiceExecutor


class ServiceExecutorCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'serviceexecutor_create.html'
    form_class = ServiceExecutorForm
    model = ServiceExecutor
    permission_required = 'serviceexecutors.can_add_serviceexecutor'

    def get_success_url(self):
        #TODO поменять url на страницу детального просмотра исполнителя
        return reverse('hostelguests:guest_list')