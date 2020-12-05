from django.urls import path
from hostelservices.views.hostelservice_list import HostelServiceListView
from hostelservices.views.hostelservice_delete import HostelServiceDeleteView
from hostelservices.views.hostelservice_detail import HostelServiceDetailView

from hostelservices.views.hostelguestservice_list import HostelServiceListView
from hostelservices.views.hostelservice_update import HostelServiceUpdateView

app_name = 'hostelservices'

urlpatterns = [
    path('hostelservices/', HostelServiceListView.as_view(), name='hostelservices_list'),
    path('hostelservices/<int:pk>/delete/', HostelServiceDeleteView.as_view(), name='hostelservice_delete'),
    path('hostelservices/<int:pk>/', HostelServiceDetailView.as_view(), name='hostelservices_detail'),
    path('hostelsercices/<int:pk>', HostelServiceUpdateView.as_view(), name='hostelservices_update'),
]