from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Patient, Request, Assistant

@receiver(post_save, sender=User)
def create_patient(sender, instance, created, **kwargs):
  if created:
    Patient.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_Patient(sender, instance, **kwargs):
  instance.patient.save()

@receiver(post_save, sender=Request)
def update_notification(sender, instance, created, **kwargs):
  if created:
    assistant = Assistant.objects.get(doctor=instance.doctor)
    assistant.notifications += 1
    assistant.save()

@receiver(post_delete, sender=Request)
def delete_notification(sender, instance, using, **kwargs):
    assistant = Assistant.objects.get(doctor=instance.doctor)
    assistant.notifications -= 1
    assistant.save()