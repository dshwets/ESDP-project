from django.urls import path

from serviceexecutors.views.serviceexecutor_create import ServiceExecutorCreateView

app_name = 'serviceexecutors'

urlpatterns = [
    path('serviceexecutors/add/', ServiceExecutorCreateView.as_view(), name='serviceexecutor_create'),
]
