from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from unwelcomeguests.models import UnwelcomeGuest


class UnwelcomeGuestDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'unwelcomeguest_delete.html'
    model = UnwelcomeGuest
    permission_required = 'unwelcomeguests.can_delete_unwelcomeguest'
    #TODO Изменить succes_url на список нежеланных гостей
    success_url = reverse_lazy('hostelguests:guest_list')
