from django.shortcuts import render, redirect
from patient.forms import RequestForm, PatientForm
from django.contrib import messages
# decorators
from django.contrib.auth.decorators import login_required
from patient.decorators import patient_only
# models
from .models import Request, Appointment, Patient

@login_required
@patient_only
def home(request):
  last_req = Request.objects.filter(patient__user__username = request.user.username).first()
  next_app = Appointment.objects.filter(request__patient__user__username = request.user.username).first()
  context = {
    'last_req': last_req,
    'next_app': next_app
  }
  return render(request, 'home.html', context)

@login_required
@patient_only
def history(request, page):
  startAt = (page-1) * 5
  endAt = startAt + 5

  histories = Request.objects.filter(patient__user__username = request.user.username)[startAt : endAt]
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
@patient_only
def makeAppointment(request):
  if request.method == 'POST':
    form = RequestForm(request.POST)
    
    if form.is_valid():
      patient = Patient.objects.get(user = request.user)
      instance = form.save(commit=False)
      instance.patient = patient
      instance.currentState = patient.currentState
      instance.save()
      messages.success(request, 'Appointment Requested')
      form = RequestForm()
    
  else: 
    form = RequestForm()

  appointments = Request.objects.filter(patient__user__username = request.user.username)[:5]
  currentState = Patient.objects.filter(user = request.user)[0].currentState

  context = {
    'form': form,
    'appointments': appointments,
    'currentState': currentState
  }
  return render(request, 'makeAppointment.html', context)

@login_required
@patient_only
def update_profile(request):
  patient = Patient.objects.get(user = request.user)
  photo = patient.picture
  if request.method == 'POST':
    form = PatientForm(request.POST, request.FILES, instance = patient)
    
    if form.is_valid():
      form.save()
      messages.success(request, 'Profile updated!')
      return redirect('update_profile')
    
  else: 
    form = PatientForm(instance = patient)
  context = {
    'form': form,
    'photo': photo
  }
  return render(request, 'update_profile.html', context)

@login_required
@patient_only
def profile(request):
  patient = Patient.objects.get(user__username = request.user.username)
  context = {
    'email': request.user.email,
    'username': request.user.username,
    'patient': patient
  }
  return render(request, 'profile.html', context)