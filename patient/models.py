from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
  GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
  )

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  fullname = models.CharField(max_length=50, null=True, blank=True)
  age = models.PositiveSmallIntegerField(null=True, blank=True)
  gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
  picture = models.ImageField(default='default.jpg')
  dob = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

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