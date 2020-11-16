from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView

from hostelguests.forms import GuestForm
from hostelguests.models import Guest


class GuestCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'guest_create.html'
    form_class = GuestForm
    model = Guest
    permission_required = 'hostelguests.can_add_guest'

    def get_success_url(self):
        return reverse('hostelguests:detail_view', kwargs={'pk': self.object.pk})