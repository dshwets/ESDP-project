from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from journalservices.forms import JournalServiceForm
from journalservices.models import JournalService


class JournalServiceUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'journalservice_update.html'
    form_class = JournalServiceForm
    model = JournalService
    permission_required = 'journalservices.can_change_journalservice'

    def get_success_url(self):
        return reverse('journalservices:journal_detail', kwargs={'pk': self.object.pk})