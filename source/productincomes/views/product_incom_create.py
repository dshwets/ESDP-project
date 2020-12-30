from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie

from serviceexecutors.models import ServiceExecutor


class IndexView(View):
    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        context={
            'serviceexecutors': ServiceExecutor.objects.all(),
            }
        return render(request, 'product_incom_create.html',context=context)