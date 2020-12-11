from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from hostelservices.models import HostelService


class HostelServiceListView(LoginRequiredMixin, ListView):
    template_name = 'hostelguestservices_list.html'
    model = HostelService
    context_object_name = 'hostel_services'
    paginate_by = 10
    paginate_orphans = 4
    ordering = ['-id']