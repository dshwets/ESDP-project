from django.conf import settings
from django.conf.urls.static import static
from hostelguests.views.guest_create import GuestCreateView
from django.urls import path, include

from hostelguests.views.guest_update import GuestUpdateView
from hostelguests.views.guestlist import GuestListView
from hostelguests.views.guestdetail import GuestDetailView
from hostelguests.views.guest_delete import GuestDeleteView

app_name = 'hostelguests'

urlpatterns = [
                  path('', GuestListView.as_view(), name='guest_list'),
                  path('guest/',
                       include(
                           [
                               path('add/', GuestCreateView.as_view(), name='guest_create'),
                               path('<int:pk>/',
                                    include(
                                        [
                                            path('detail/', GuestDetailView.as_view(), name='detail_view'),
                                            path('delete/', GuestDeleteView.as_view(), name='guest_delete'),
                                            path('delete/', GuestUpdateView.as_view(), name='guest_update'),
                                            path('note/', include(('aboutguests.urls', 'aboutguests'), namespace="note"))
                                        ],
                                    ),
                                    )
                           ],
                       ),
                       ),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
