from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from hostelservices.models import HostelService


class HostelServiceDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'hostelservice_delete.html'
    model = HostelService
    permission_required = 'hostelservices.can_delete_hostelservice'
    success_url = reverse_lazy('hostelservices:hostelservices_list')