from django.urls import path
from hostelservices.views.hostelservice_delete import HostelServiceDeleteView
from hostelservices.views.hostelservice_detail import HostelServiceDetailView
from hostelservices.views.hostelservice_list import HostelServiceListView
from hostelservices.views.hostelservice_update import HostelServiceUpdateView
from hostelservices.views.hostelservices_create import HostelServiceCreateView


app_name = 'hostelservices'

urlpatterns = [
    path('hostelservices/', HostelServiceListView.as_view(), name='hostelservices_list'),
    path('hostelservices/<int:pk>/update/', HostelServiceUpdateView.as_view(), name='hostelservices_update'),
    path('hostelservices/<int:pk>/delete/', HostelServiceDeleteView.as_view(), name='hostelservice_delete'),
    path('hostelservices/<int:pk>/', HostelServiceDetailView.as_view(), name='hostelservices_detail'),
    path('hostelservices/add', HostelServiceCreateView.as_view(), name='hostelservices_add'),
]