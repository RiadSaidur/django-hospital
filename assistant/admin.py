from django.contrib import admin
from assistant.models import Assistant, Doctor

class AssistantAdmin(admin.ModelAdmin):
  fields = ['user', 'doctor']

class DoctorAdmin(admin.ModelAdmin):
  fields = ['name', 'max_slots', 'available']

admin.site.register(Assistant, AssistantAdmin)
admin.site.register(Doctor, DoctorAdmin)