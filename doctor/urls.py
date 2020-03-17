from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import index, signup, makeAppointment

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('signin/', LoginView.as_view(template_name = 'signin.html'), name='signin'),
    path('signout/', LogoutView.as_view(template_name = 'signout.html'), name='signout'),
    path('appointment/', makeAppointment, name='makeAppointment')
]