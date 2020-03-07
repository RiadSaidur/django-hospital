from django.shortcuts import render, HttpResponse
from doctor.models import AppointmentForm

def index(request):
  context = {
    'form': AppointmentForm()
  }
  print(request)
  return render(request, 'index.html')