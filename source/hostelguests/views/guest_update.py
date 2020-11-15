from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from hostelguests.forms import GuestForm
from hostelguests.models import Guest


class GuestUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'guest_update.html'
    form_class = GuestForm
    model = Guest
    permission_required = 'hostelguests.can_change_guest'

    def get_success_url(self):
        return reverse('hostelguests:detail_view', kwargs={'pk': self.object.pk})
