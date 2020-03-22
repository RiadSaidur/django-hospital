from django.contrib import admin
from .models import Patient, Request, Appointment

class PatientAdmin(admin.ModelAdmin):
  fields = ['user', 'fullname', 'dob', 'age', 'gender', 'picture']

class RequestAdmin(admin.ModelAdmin):
  fields = ['confirmed', 'patient', 'doctor']

class AppointmentAdmin(admin.ModelAdmin):
  fields = ['request']

admin.site.register(Patient, PatientAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Appointment, AppointmentAdmin)