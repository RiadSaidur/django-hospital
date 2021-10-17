from django.shortcuts import render, redirect
from django.contrib import messages
from users.decorators import only_unauthenticated
from users.forms import UserRegistrationForm
#for checking username availability only
from django.http import JsonResponse
from django.contrib.auth.models import User

@only_unauthenticated
def index(request):
  context = {}
  return render(request, 'users/index.html', context)

@only_unauthenticated
def signup(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      messages.success(request, 'You can Sign In now')
      return redirect('signin')
  else:
    form = UserRegistrationForm()

  context = {
    'form': form
  }

  return render(request, 'users/signup.html', context)

def checkUsername(request, desiredUsername):
  if request.method == 'GET':
    if not User.objects.filter(username = desiredUsername).exists():
      return JsonResponse({'isAvailable': True})
    # returns false if username exists 
    return JsonResponse({'isAvailable': False})