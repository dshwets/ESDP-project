from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from hostelguests.models import Guest


class GuestDetailView(LoginRequiredMixin, DetailView):
    model = Guest
    template_name = 'view/../templates/guest_detail_view.html'