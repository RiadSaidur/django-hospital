from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Patient

@receiver(post_save, sender=User)
def create_patient(sender, instance, created, **kwargs):
    if created:
        print("NICE")
        Patient.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_Patient(sender, instance, **kwargs):
    instance.patient.save()