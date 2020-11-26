from django.views.generic import DetailView

from serviceexecutors.models import ServiceExecutor


class ServiceExecutorDetailView(DetailView):
    template_name = 'serviceexecutor_detail.html'
    model = ServiceExecutor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
