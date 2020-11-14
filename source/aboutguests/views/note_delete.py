from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import DeleteView
from aboutguests.models import Note


class NoteDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'note_delete.html'
    model = Note
    permission_required = 'aboutguests.can_delete_note'

    def get_success_url(self):
        return reverse('hostelguests:detail_view', kwargs={'pk': self.object.guest.pk})
