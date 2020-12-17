from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from journalservices.models import JournalService


class JournalServiceDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'journalservice_delete.html'
    model = JournalService
    permission_required = 'journalservices.can_delete_journalservice'
    success_url = reverse_lazy('journalservices:journal_list')
