from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import makeAppointment, update_profile, profile, history, home

urlpatterns = [
    path('home/', home, name='home'),
    path('history/<int:page>', history, name='history'),
    path('profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('appointment/', makeAppointment, name='makeAppointment')
]