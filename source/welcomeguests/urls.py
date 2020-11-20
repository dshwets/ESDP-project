from django.conf import settings
from django.conf.urls.static import static
from welcomeguests.views.welcomeguest_list import WelcomeGuestListView
from welcomeguests.views.welcomeguest_delete import WelcomeGuestDeleteView
from django.urls import path



app_name = 'welcomeguests'

urlpatterns = [
    path('welcomeguests/<int:pk>/delete/', WelcomeGuestDeleteView.as_view(), name='welcomeguest_delete'),
    path('welcomeguest/', WelcomeGuestListView.as_view(), name='welcome_guest_list'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)