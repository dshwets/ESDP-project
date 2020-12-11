from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from hostelguests.models import Guest
from unwelcomeguests.models import UnwelcomeGuest
from welcomeguests.forms import WelcomeGuestForm
from welcomeguests.models import WelcomeGuest


class WelcomeGuestCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'welcomeguest_create.html'
    form_class = WelcomeGuestForm
    model = WelcomeGuest
    permission_required = 'welcomeguests.can_add_welcomeguest'

    def form_valid(self, form):
        guest = get_object_or_404(Guest, pk=self.kwargs.get('pk'))
        unwelcome = UnwelcomeGuest.objects.filter(guest=guest)
        if unwelcome:
            unwelcome[0].delete()
        welcomeguest = form.save(commit=False)
        welcomeguest.guest = guest
        welcomeguest.created_by_id = self.request.user.pk
        welcomeguest.save()
        return HttpResponseRedirect(reverse('hostelguests:detail_view', kwargs={'pk': guest.pk}))