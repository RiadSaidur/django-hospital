from django.contrib import admin

from .models import Patient, Assistant, Doctor, Appointment

class PatientAdmin(admin.ModelAdmin):
  fields = ['user', 'age', 'gender']

class AssistantAdmin(admin.ModelAdmin):
  fields = ['name', 'docid']

class DoctorAdmin(admin.ModelAdmin):
  fields = ['name']

class AppointmentAdmin(admin.ModelAdmin):
  fields = ['confirmed', 'patid', 'docid', 'assid']

admin.site.register(Patient, PatientAdmin)
admin.site.register(Assistant, AssistantAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)