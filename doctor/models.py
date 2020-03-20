from django.db import models
from django.contrib.auth.models import User
from assistant.models import Doctor

class Patient(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  age = models.PositiveSmallIntegerField(null=True, blank=True)
  gender = models.CharField(max_length=1, null=True, blank=True)

  def __str__(self):
    return str(self.user.username)

class Request(models.Model):
  confirmed = models.BooleanField(default=False)
  patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
  doctor = models.ForeignKey('assistant.Doctor', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f'{self.doctor} - {self.created_at}'

class Appointment(models.Model):
  request = models.ForeignKey('Request', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.request.doctor} - {self.request.patient}'