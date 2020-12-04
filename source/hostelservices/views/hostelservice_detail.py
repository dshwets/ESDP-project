from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView

from hostelservices.models import HostelService


class ServiceExecutorDetailView(PermissionRequiredMixin,DetailView):
    template_name = 'serviceexecutor_detail.html'
    model = HostelService
    permission_required = 'hostelservice.can_view_hostelservice'
#    paginate_documents_by = 5
#    paginate_documents_orphans = 0