from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  age = models.PositiveSmallIntegerField(null=True, blank=True)
  gender = models.CharField(max_length=1, null=True, blank=True)

  def __str__(self):
    return str(self.user.username)

class Doctor(models.Model):
  name = models.CharField(max_length=50)
  max_slots = models.PositiveIntegerField(default=10)
  available = models.PositiveIntegerField(default=0)

  def __str__(self):
    return str(self.name)

class Assistant(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
  notifications = models.PositiveIntegerField(default=0)

  def __str__(self):
    return str(self.user.username)

class Request(models.Model):
  confirmed = models.BooleanField(default=False)
  patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
  doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.doctor} - {self.created_at}'

class Appointment(models.Model):
  request = models.ForeignKey('Request', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.request.doctor} - {self.request.patient}'