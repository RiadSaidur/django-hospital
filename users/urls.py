from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import index, signup, checkUsername

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('signin/', LoginView.as_view(template_name = 'users/signin.html', redirect_authenticated_user=True), name='signin'),
    path('signout/', LogoutView.as_view(template_name = 'users/index.html'), name='signout'),
    path('api/checkUsername/<str:desiredUsername>', checkUsername, name='checkUsername'),
]