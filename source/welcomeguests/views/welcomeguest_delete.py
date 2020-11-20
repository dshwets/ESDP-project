from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from welcomeguests.models import WelcomeGuest


class UnwelcomeGuestDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'welcomeguest_delete.html'
    model = WelcomeGuest
    permission_required = 'welcomeguests.can_delete_welcomeguest'
    success_url = reverse_lazy('hostelguests:guest_list')
