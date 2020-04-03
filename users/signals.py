# signals
from django.db.models.signals import post_save
from django.dispatch import receiver
# models
from django.contrib.auth.models import User
from patient.models import Patient

@receiver(post_save, sender=User)
def create_patient(sender, instance, created, **kwargs):
  if created:
    Patient.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_Patient(sender, instance, **kwargs):
  instance.patient.save()