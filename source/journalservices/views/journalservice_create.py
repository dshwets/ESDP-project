from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from journalservices.forms import JournalServiceForm
from journalservices.models import JournalService


class JournalServiceCreateView(PermissionRequiredMixin, CreateView):
    model = JournalService
    form_class = JournalServiceForm
    template_name = ' journalservice_create.html'
    permission_required = 'journalservices.can_add_journalservice'
    success_url = reverse_lazy('journalservices:journal_list')

    def get_form_kwargs(self):
        kwargs = super(JournalServiceCreateView, self).get_form_kwargs()
        guest_id = self.kwargs.get('guest_pk')
        kwargs.update({
            'guest_id': guest_id,
        })
        return kwargs
