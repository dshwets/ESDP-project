from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from journalservices.models import JournalService


class JournalServicesListView(LoginRequiredMixin, ListView):
    template_name = 'journalservices_list.html'
    queryset = JournalService.objects.order_by('-created_at')
    context_object_name = 'journalservices'
    paginate_by = 30
    paginate_orphans = 4