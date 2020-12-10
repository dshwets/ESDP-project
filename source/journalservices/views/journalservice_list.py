from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from journalservices.models import JournalService


class JournalServicesListView(PermissionRequiredMixin, ListView):
    template_name = 'journalservices_list.html'
    queryset = JournalService.objects.order_by('-created_at')
    context_object_name = 'journals'
    permission_required = 'journalservices.can_view_journalservice'
    paginate_by = 30
    paginate_orphans = 4