from django.shortcuts import render, redirect
from doctor.forms.registerFrom import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def makeAppointment(request):
  context = {}
  return render(request, 'makeAppointment.html', context)

def index(request):
  return render(request, 'index.html')

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

  return render(request, 'signup.html', context)