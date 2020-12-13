from django.urls import path

from journalservices.views.journalservice_create import JournalServiceCreateView
from journalservices.views.journalservice_list import JournalServicesListView
from journalservices.views.journalservice_detail import JournalServiceDetailView
from journalservices.views.journalservice_delete import JournalServiceDeleteView
from journalservices.views.journalservice_update import JournalServiceUpdateView


app_name = 'journalservices'

urlpatterns = [
    path('journal/', JournalServicesListView.as_view(), name='journal_list'),
    path('journal/<int:pk>/', JournalServiceDetailView.as_view(), name='journal_detail'),
    path('journal/<int:pk>/delete/', JournalServiceDeleteView.as_view(), name='journal_delete'),
    path('guest/<int:guest_pk>/journal_add', JournalServiceCreateView.as_view(), name='journal_create'),
    path('journal/<int:pk>/update', JournalServiceUpdateView.as_view(), name='journal_update'),
]