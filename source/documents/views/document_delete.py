from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from documents.models import Document


class DocumentDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Document
    permission_required = 'documents.can_delete_document'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        pk = self.object.service_executor.pk
        self.object.service_executor = None
        self.object.save()
        return HttpResponseRedirect(reverse('serviceexecutors:serviceexecutor_view', kwargs={'pk': pk}))
