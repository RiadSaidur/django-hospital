from django.shortcuts import render, redirect
from doctor.forms import UserRegistrationForm, RequestForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Request, Appointment, Patient

@login_required
def history(request, page):
  startAt = page + 4
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