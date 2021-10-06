# signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# models
from django.contrib.auth.models import User
from .models import Request, Appointment
from assistant.models import Assistant, Doctor

@receiver(post_save, sender=Request)
def update_notification(sender, instance, created, **kwargs):
  if created:
    assistant = Assistant.objects.get(doctor=instance.doctor)
    assistant.notifications += 1
    assistant.save()
  else:
    try:
      appointment = Appointment.objects.get(request = instance)
      if instance.confirmed and not appointment:
        Appointment.objects.create(request = instance)
      if not instance.confirmed and appointment:
          appointment.delete()
    except Appointment.DoesNotExist:
      print("error")

@receiver(post_delete, sender=Request)
def delete_notification(sender, instance, using, **kwargs):
    assistant = Assistant.objects.get(doctor=instance.doctor)
    assistant.notifications -= 1
    assistant.save()

@receiver(post_save, sender=Appointment)
def update_slots(sender, instance, created, **kwargs):
  if created:
    doctor = Doctor.objects.get(name=instance.request.doctor)
    doctor.available -= 1
    doctor.save()

@receiver(post_delete, sender=Appointment)
def delete_slots(sender, instance, using, **kwargs):
    doctor = Doctor.objects.get(name=instance.request.doctor)
    doctor.available += 1
    doctor.save()