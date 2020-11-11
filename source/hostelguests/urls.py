from django.urls import path

from hostelguests.views.guestlist import GuestListView
from hostelguests.views.guestdetail import GuestDetailView

app_name = 'hostelguests'

urlpatterns = [
    path('', GuestListView.as_view(), name='guest_list'),
    path('<int:pk>/detail', GuestDetailView.as_view(), name='detail_view'),
]