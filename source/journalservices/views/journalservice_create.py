from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

from hostelguests.models import Guest
from journalservices.forms import JournalServiceForm
from journalservices.models import JournalService


class JournalServiceView(PermissionRequiredMixin, CreateView):
    model = JournalService
    form_class = JournalServiceForm
    template_name = ' journalservice_create.html'
    permission_required = 'journalservices.can_add_journalservice'

    def form_valid(self, form):
        guest = get_object_or_404(Guest, pk=self.kwargs.get('guest_pk'))
        journal = form.save(commit=False)
        journal.guest = guest
        journal.save()
        return redirect(
            'journalservices:journal_list',
        )