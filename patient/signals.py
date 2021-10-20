# signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# models
from .models import Request, Appointment
from assistant.models import Assistant, Doctor
# for appointment dates
from datetime import timedelta, time, datetime

def getNextDayDatetime(lastAppointment=None, newDay=False):
  newDate = datetime.now()
  newTime = time(17, 0, 0)

  if newDay:
    maxAppTime = time(20, 0, 0)
    nextAppTime = lastAppointment.appointmentDate + timedelta(minutes=30)
    if nextAppTime.time() > maxAppTime:
      return lastAppointment.appointmentDate + timedelta(days=1) - timedelta(hours=3)
    else:
      return nextAppTime
      

  nextDayDatetime = datetime(newDate.year, newDate.month, newDate.day + 1, newTime.hour, newTime.minute, newTime.second)
  return nextDayDatetime

def getNextAppointmentDatetime():
  lastAppointment = Appointment.objects.order_by('-created_at').first()

  if lastAppointment:
    minAppTime = time(17, 0, 0)
    maxAppTime = time(20, 0, 0)

    nextAppTime = lastAppointment.appointmentDate + timedelta(minutes=30)

    if nextAppTime.time() > maxAppTime:
      nextAppTime = getNextDayDatetime(lastAppointment, True)
    
    return nextAppTime
  else:
    return getNextDayDatetime()

@receiver(post_save, sender=Request)
def update_notification(sender, instance, created, **kwargs):
  if created:
    assistant = Assistant.objects.get(doctor=instance.doctor)
    assistant.save()
  else:
    try:
      appointment = Appointment.objects.get(request = instance)
      if not instance.confirmed and appointment:
          appointment.delete()
    except Appointment.DoesNotExist:
      if instance.confirmed:
        Appointment.objects.create(request = instance, appointmentDate= getNextAppointmentDatetime())


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