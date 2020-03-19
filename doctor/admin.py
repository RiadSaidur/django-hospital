from django.contrib import admin

from .models import Patient, Assistant, Doctor, Request, Appointment

class PatientAdmin(admin.ModelAdmin):
  fields = ['user', 'age', 'gender']

class AssistantAdmin(admin.ModelAdmin):
  fields = ['user', 'doctor', 'notifications']

class DoctorAdmin(admin.ModelAdmin):
  fields = ['name']

class RequestAdmin(admin.ModelAdmin):
  fields = ['confirmed', 'patient', 'doctor']

class AppointmentAdmin(admin.ModelAdmin):
  fields = ['request']

admin.site.register(Patient, PatientAdmin)
admin.site.register(Assistant, AssistantAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Appointment, AppointmentAdmin)