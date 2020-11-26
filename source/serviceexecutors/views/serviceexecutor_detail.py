from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView

from serviceexecutors.models import ServiceExecutor


class ServiceExecutorDetailView(PermissionRequiredMixin,DetailView):
    template_name = 'serviceexecutor_detail.html'
    model = ServiceExecutor
    permission_required = 'serviceexecutors.can_view_serviceexecutor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
