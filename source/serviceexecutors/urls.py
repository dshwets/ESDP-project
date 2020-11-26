from django.urls import path

from serviceexecutors.views.serviceexecutor_create import ServiceExecutorCreateView
from serviceexecutors.views.serviceexecutor_detail import ServiceExecutorDetailView
from serviceexecutors.views.serviceexecutor_update import ServiceExecutorUpdateView

app_name = 'serviceexecutors'

urlpatterns = [
    path('serviceexecutors/add/', ServiceExecutorCreateView.as_view(), name='serviceexecutor_create'),
    path('serviceexecutors/<int:pk>/', ServiceExecutorDetailView.as_view(), name='serviceexecutor_view'),
    path('serviceexecutors/<int:pk>/update/', ServiceExecutorUpdateView.as_view(), name='serviceexecutor_update'),
]
