from django.urls import path

from hostelservices.views.hostelguestservice_list import HostelServiceListView

app_name = 'hostelservices'

urlpatterns = [
    path('hostelservices/', HostelServiceListView.as_view(), name='hostelservices_list'),
]