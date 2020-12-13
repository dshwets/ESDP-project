from django.urls import path

from journalservices.views.journalservice_create import JournalServiceCreateView
from journalservices.views.journalservice_list import JournalServicesListView
from journalservices.views.journalservice_detail import JournalServiceDetailView

app_name = 'journalservices'

urlpatterns = [
    path('journal/', JournalServicesListView.as_view(), name='journal_list'),
    path('journal/<int:pk>/', JournalServiceDetailView.as_view(), name='journal_detail'),
    path('guest/<int:guest_pk>/journal_add', JournalServiceCreateView.as_view(), name='journal_create'),
]