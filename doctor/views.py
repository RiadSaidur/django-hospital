from django.shortcuts import render, redirect
from doctor.forms.registerFrom import UserRegistrationForm
from django.contrib import messages

def index(request):
  return render(request, 'index.html')

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      print('NICE')
      messages.success(request, 'NICE BRO!')
      return redirect('index')
  else:
    form = UserRegistrationForm()

  context = {
    'form': form
  }

  return render(request, 'register.html', context)