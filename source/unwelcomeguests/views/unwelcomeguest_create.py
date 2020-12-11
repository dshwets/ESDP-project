from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from hostelguests.models import Guest
from unwelcomeguests.forms import UnWelcomeGuestForm
from unwelcomeguests.models import UnwelcomeGuest
from welcomeguests.models import WelcomeGuest


class UnWelcomeGuestCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'unwelcome_create.html'
    form_class = UnWelcomeGuestForm
    model = UnwelcomeGuest
    permission_required = 'unwelcomeguests.can_add_unwelcomeguest'

    def form_valid(self, form):
        guest = get_object_or_404(Guest, pk=self.kwargs.get('pk'))
        welcome = WelcomeGuest.objects.filter(guest=guest)
        if welcome:
            welcome[0].delete()
        unwelcomeguest = form.save(commit=False)
        unwelcomeguest.guest = guest
        unwelcomeguest.save()
        return HttpResponseRedirect(reverse('hostelguests:detail_view', kwargs={'pk': guest.pk}))