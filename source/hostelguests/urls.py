from django.urls import path

from hostelguests.views.guestlist import GuestListView
from hostelguests.views.guest_delete import GuestDeleteView

app_name = 'hostelguests'

urlpatterns = [
    path('', GuestListView.as_view(), name='guest_list'),
    path('<int:pk>/delete/', GuestDeleteView.as_view(), name='guest_delete'),
]