from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView
from django.core.paginator import Paginator
from serviceexecutors.models import ServiceExecutor


class ServiceExecutorDetailView(PermissionRequiredMixin,DetailView):
    template_name = 'serviceexecutor_detail.html'
    model = ServiceExecutor
    permission_required = 'serviceexecutors.can_view_serviceexecutor'
    paginate_documents_by = 5
    paginate_documents_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents, page, is_paginated = self.paginate_documents(self.object)
        context['documents'] = documents
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        return context

    def paginate_documents(self, serviceexecutor):
        documents = serviceexecutor.documents.all().order_by('-created_at')
        if documents.count() > 0:
            paginator = Paginator(documents, self.paginate_documents_by, orphans=self.paginate_documents_orphans)
            page_number = self.request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            is_paginated = paginator.num_pages > 1
            return page.object_list, page, is_paginated
        else:
            return documents, None, False
