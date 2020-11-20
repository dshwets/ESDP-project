

from django.urls import path



from welcomeguests.views.welcomeguest_delete import WelcomeGuestDeleteView

app_name = 'welcomeguests'

urlpatterns = [
    path('welcomeguests/<int:pk>/delete/', WelcomeGuestDeleteView.as_view(), name='welcomeguest_delete'),

    ]