from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from serviceexecutors.models import ServiceExecutor


class ServiceExecutorsGuestListView(LoginRequiredMixin, ListView):
    template_name = 'serviceexecutor_list.html'
    queryset = ServiceExecutor.objects.all()
    context_object_name = 'service_executors'
    paginate_by = 10
    paginate_orphans = 4
