from django.shortcuts import render, redirect
from doctor.forms.registerFrom import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Appointment

@login_required
def makeAppointment(request):
  context = {}
  return render(request, 'makeAppointment.html', context)

@login_required
def create_profile(request):
  context = {}
  return render(request, 'create_profile.html', context)

@login_required
def profile(request):
  app = Appointment.objects.filter(patid__user__username=request.user.username)
  print(app)
  context = {
    'fullname': request.user.get_full_name(),
    'email': request.user.email,
    'username': request.user.username
  }
  return render(request, 'profile.html', context)

def index(request):
  context = {}
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