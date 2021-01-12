from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from documents.models import Document
from serviceexecutors.models import ServiceExecutor


class ServiceExecutorDetailView(PermissionRequiredMixin, DetailView, MultipleObjectMixin):
    template_name = 'serviceexecutor_detail.html'
    model = ServiceExecutor
    permission_required = 'serviceexecutors.can_view_serviceexecutor'
    paginate_by = 5
    paginate_orphans = 0

    def get_context_data(self, **kwargs):
        object_list = Document.objects.filter(service_executor=self.get_object()).order_by('-pk')
        context = super(ServiceExecutorDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context

