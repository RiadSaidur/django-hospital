from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import index

app_name = 'assistant'
urlpatterns = [
    path('', index, name='index'),
]