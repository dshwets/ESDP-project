from django.urls import path

from serviceexecutors.views.serviceexecutor_create import ServiceExecutorCreateView
from serviceexecutors.views.serviceexecutor_update import ServiceExecutorUpdateView

app_name = 'serviceexecutors'

urlpatterns = [
    path('serviceexecutors/add/', ServiceExecutorCreateView.as_view(), name='serviceexecutor_create'),
    path('serviceexecutors/update/', ServiceExecutorUpdateView.as_view(), name='serviceexecutor_update'),
]
