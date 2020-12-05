from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from documents.forms import DocumentForm
from documents.models import Document


class DocumentUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'document_update.html'
    form_class = DocumentForm
    model = Document
    permission_required = 'documents.can_change_document'

    def get_success_url(self):
        return reverse('serviceexecutors:serviceexecutor_view', kwargs={'pk': self.object.service_executor.pk})
