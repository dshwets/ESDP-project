from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from hostelservices.forms import HostelServiceMultiForm
from hostelservices.models import HostelService


class HostelServiceCreateView(PermissionRequiredMixin, CreateView):
    model = HostelService
    form_class = HostelServiceMultiForm
    template_name = 'hostelservices_create.html'
    permission_required = 'hostelservices.can_add_hostelservice'
    success_url = reverse_lazy('hostelservices:hostelservices_list')