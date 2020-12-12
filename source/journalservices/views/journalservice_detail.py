from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView
from journalservices.models import JournalService


class JournalServiceDetailView(PermissionRequiredMixin,DetailView):
    template_name = 'journalservice_detail.html'
    model = JournalService
    permission_required = 'journalservices.can_view_journalservice'