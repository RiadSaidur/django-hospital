from django.db import models
from django.contrib.auth.models import User

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