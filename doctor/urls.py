from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import index, signup, makeAppointment, update_profile, profile, history, home

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('history/<int:page>', history, name='history'),
    path('profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('signup/', signup, name='signup'),
    path('signin/', LoginView.as_view(template_name = 'signin.html', redirect_authenticated_user=True), name='signin'),
    path('signout/', LogoutView.as_view(template_name = 'signout.html'), name='signout'),
    path('appointment/', makeAppointment, name='makeAppointment')
]