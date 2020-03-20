from django.shortcuts import render, redirect
from doctor.forms.registerFrom import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Request, Appointment

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
  context = {
    'fullname': request.user.get_full_name(),
    'email': request.user.email,
    'username': request.user.username
  }
  return render(request, 'profile.html', context)

def index(request):
  prev_app = Request.objects.filter(patient__user__username = request.user.username).first()
  next_app = Appointment.objects.filter(request__patient__user__username = request.user.username).first()
  context = {
    'prev_app': prev_app,
    'next_app': next_app
  }
  print(next_app)
  return render(request, 'index.html', context)

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