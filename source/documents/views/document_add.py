from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from documents.forms import DocumentForm
from documents.models import Document
from serviceexecutors.models import ServiceExecutor
from django.http import HttpResponseRedirect


class DocumentExecutorCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'document_add.html'
    form_class = DocumentForm
    model = Document
    permission_required = 'documents.can_add_document'

    def form_valid(self, form):
        document = form.save(commit=False)
        service_executor = get_object_or_404(ServiceExecutor, pk=self.kwargs.get('pk'))
        document.service_executor = service_executor
        document.save()
        return HttpResponseRedirect(
            reverse(
                'serviceexecutors:serviceexecutor_view',
                kwargs={'pk': service_executor.pk}
            )
        )
