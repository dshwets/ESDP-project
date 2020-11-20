from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView

from hostelguests.models import Guest
from welcomeguests.forms import WelcomeGuestForm
from welcomeguests.models import WelcomeGuest


class WelcomeGuestCreateView(CreateView):
    template_name = 'welcomeguest_create.html'
    form_class = WelcomeGuestForm
    model = WelcomeGuest

    def form_valid(self, form):
        guest = get_object_or_404(Guest, pk=self.kwargs.get('pk'))
        welcomeguest = form.save(commit=False)
        welcomeguest.guest = guest
        welcomeguest.save()
        return HttpResponseRedirect(reverse('hostelguests:detail_view', kwargs={'pk': guest.pk}))