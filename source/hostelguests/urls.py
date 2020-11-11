from django.urls import path

from hostelguests.views.guestlist import GuestListView
from hostelguests.views.guest_detail import Guest_Detail_View

app_name = 'hostelguests'

urlpatterns = [
    path('', GuestListView.as_view(), name='guest_list'),
    path('/<int:pk>/detail', Guest_Detail_View.as_view(), name='detail_view'),
]