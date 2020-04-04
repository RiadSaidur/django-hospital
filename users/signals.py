# signals
from django.db.models.signals import post_save
from django.dispatch import receiver
# models
from django.contrib.auth.models import User
from patient.models import Patient
# groups
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def create_patient(sender, instance, created, **kwargs):
  if created:
    Patient.objects.create(user=instance)
    group = Group.objects.get(name='patient')
    instance.groups.add(group)

@receiver(post_save, sender=User)
def save_Patient(sender, instance, **kwargs):
  instance.patient.save()