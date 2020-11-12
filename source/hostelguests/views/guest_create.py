from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from hostelguests.forms import GuestForm
from hostelguests.models import Guest


class GuestCreateView(PermissionRequiredMixin,CreateView):
    template_name = 'guest_create.html'
    form_class = GuestForm
    model = Guest
    permission_required = 'hostelguests.can_add_guest'
    #TODO after create DetailGuestView need to chage url
    success_url = reverse_lazy('hostelguests:guest_list')