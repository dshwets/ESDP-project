import base64

from django.core.files.base import ContentFile
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.utils import timezone

from hostelguests.forms import GuestForm
from hostelguests.models import Guest


class GuestCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'guest_create.html'
    form_class = GuestForm
    model = Guest
    permission_required = 'hostelguests.can_add_guest'

    def form_valid(self, form):
        guest = form.save(commit=False)
        print(form.cleaned_data['hidden_base64'])
        if form.cleaned_data['hidden_base64'] != '':
            photo_base64 = form.cleaned_data['hidden_base64']
            format, imgstr = photo_base64.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'photo_{timezone.now()}.' + ext)
            guest.photo = data
        else:
            super.form_valuid(self,form)
        guest.save()
        return redirect('hostelguests:detail_view', pk=guest.pk)

    def get_success_url(self):
        return reverse('hostelguests:detail_view', kwargs={'pk': self.object.pk})