from django.shortcuts import render, redirect
from doctor.forms import UserRegistrationForm, RequestForm, PatientForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Request, Appointment, Patient
from doctor.decorators import only_unauthenticated

@login_required
def home(request):
  prev_app = Request.objects.filter(patient__user__username = request.user.username).first()
  next_app = Appointment.objects.filter(request__patient__user__username = request.user.username).first()
  context = {
    'prev_app': prev_app,
    'next_app': next_app
  }
  return render(request, 'home.html', context)

@login_required
def history(request, page):
  startAt = (page-1) * 5
  endAt = startAt + 5

  histories = Request.objects.all()[startAt : endAt]
  more = histories.count() == 5

  context = {
    'histories': histories,
    'next': page + 1,
    'prev': page-1 or page,
    'more': more,
    'page': page
  }
  return render(request, 'history.html', context)

@login_required
def makeAppointment(request):
  if request.method == 'POST':
    form = RequestForm(request.POST)
    
    if form.is_valid():
      patient = Patient.objects.get(user = request.user)
      instance = form.save(commit=False)
      instance.patient = patient
      instance.save()
      messages.success(request, 'Appointment Requested')
      form = RequestForm()
    
  else: 
    form = RequestForm()

  appointments = Request.objects.all()[:5]

  context = {
    'form': form,
    'appointments': appointments
  }
  return render(request, 'makeAppointment.html', context)

@login_required
def update_profile(request):
  patient = Patient.objects.get(user = request.user)
  photoURL = patient.picture.url
  if request.method == 'POST':
    form = PatientForm(request.POST, instance = patient)
    
    if form.is_valid():
      form.save()
      messages.success(request, 'Profile updated!')
    
  else: 
    form = PatientForm(instance = patient)
  context = {
    'form': form,
    'photoURL': photoURL
  }
  return render(request, 'update_profile.html', context)

@login_required
def profile(request):
  patient = Patient.objects.get(user__username = request.user.username)
  context = {
    'email': request.user.email,
    'username': request.user.username,
    'patient': patient
  }
  return render(request, 'profile.html', context)

@only_unauthenticated
def index(request):
  context = {}
  return render(request, 'index.html', context)

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

  return render(request, 'signup.html', context)