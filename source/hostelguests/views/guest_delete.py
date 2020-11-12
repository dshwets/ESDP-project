from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from hostelguests.models import Guest


class GuestDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'guest_delete.html'
    model = Guest
    permission_required = 'hostelguests.can_delete_guest'
    success_url = reverse_lazy('hostelguests:guest_list')
