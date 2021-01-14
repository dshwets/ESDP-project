from hostelguests.views.guest_birthday import GuestBirthdayListView
from hostelguests.views.guest_create import GuestCreateView
from django.urls import path, include

from hostelguests.views.guest_update import GuestUpdateView
from hostelguests.views.guestlist import GuestListView
from hostelguests.views.guestdetail import GuestDetailView
from hostelguests.views.guest_delete import GuestDeleteView
from unwelcomeguests.views.unwelcomeguest_create import UnWelcomeGuestCreateView
from welcomeguests.views.welcomeguest_create import WelcomeGuestCreateView

app_name = 'hostelguests'

urlpatterns = [
                  path('', GuestListView.as_view(), name='guest_list'),
                  path('guest/birthday/', GuestBirthdayListView.as_view(), name='guest_birthday_list'),
                  path('guest/',
                       include(
                           [
                               path('add/', GuestCreateView.as_view(), name='guest_create'),
                               path('<int:pk>/',
                                    include(
                                        [
                                            path('detail/', GuestDetailView.as_view(), name='detail_view'),
                                            path('delete/', GuestDeleteView.as_view(), name='guest_delete'),
                                            path('update/', GuestUpdateView.as_view(), name='guest_update'),
                                            path('welcomeguests/add', WelcomeGuestCreateView.as_view(),
                                                 name='welcomeguest_create'),
                                            path('unwelcomeguest/add', UnWelcomeGuestCreateView.as_view(),
                                                 name='unwelcomeguest_create'),
                                        ],
                                    ),
                                    )
                           ],
                       ),
                  ),
              ]
