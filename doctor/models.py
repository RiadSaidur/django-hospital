from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Patient(models.Model):
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  fullname = models.CharField(max_length=50)
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
  name =  models.CharField(max_length=50)
  docid = models.ForeignKey('Doctor', on_delete=models.CASCADE)

  def __str__(self):
    return str(self.name)

class Appointment(models.Model):
  confirmed = models.BooleanField(default=False)
  patid = models.OneToOneField('Patient', on_delete=models.CASCADE)
  docid = models.ForeignKey('Doctor', on_delete=models.CASCADE)
  assid = models.ForeignKey('Assistant', on_delete=models.CASCADE)

  def __str__(self):
    return str(self.patid)

class AppointmentForm(ModelForm):
  class Meta:
    model = Appointment
    fields = ['patid', 'docid', 'assid']