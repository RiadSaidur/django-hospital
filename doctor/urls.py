from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import index, signup, makeAppointment, create_profile, profile, history

urlpatterns = [
    path('', index, name='index'),
    path('history/<int:page>', history, name='history'),
    path('profile/', profile, name='profile'),
    path('create_profile/', create_profile, name='create_profile'),
    path('signup/', signup, name='signup'),
    path('signin/', LoginView.as_view(template_name = 'signin.html'), name='signin'),
    path('signout/', LogoutView.as_view(template_name = 'signout.html'), name='signout'),
    path('appointment/', makeAppointment, name='makeAppointment')
]