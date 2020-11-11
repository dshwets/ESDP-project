from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView

from hostelguests.models import Guest


class GuestDetailView(PermissionRequiredMixin, DetailView):
    model = Guest
    template_name = 'guestdetail.html'
    permission_required = 'сan_view_guest'