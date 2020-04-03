from django.shortcuts import render, redirect
from django.contrib import messages
from users.decorators import only_unauthenticated
from users.forms import UserRegistrationForm

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