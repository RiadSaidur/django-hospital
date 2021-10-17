from django.shortcuts import render, redirect
# decorators
from django.contrib.auth.decorators import login_required
from assistant.decorators import assistant_only
# models
from patient.models import Request, Appointment
from assistant.models import Assistant, Doctor
# date-time
from django.utils import timezone
# forms
from assistant.forms import RequestApproveForm

def saveRequest (req, data, pk):
  req = Request.objects.get(pk=pk)
  print(req, data, pk)
  if req:
    form = RequestApproveForm(data, instance=req)
    if form.is_valid():
      form.save()
      redirect('assistant:index')

@login_required
@assistant_only
def index(request):
  assistant = Assistant.objects.get(user=request.user)
  reqs = Request.objects.filter(doctor = assistant.doctor, created_at__date__gte = timezone.now().date()).order_by('created_at')
  # accepts = Request.objects.filter(doctor = assistant.doctor, confirmed = True, created_at__date__gte = timezone.now().date()).order_by('created_at')

  reqsForms = []
  acceptsForm = []

  pk = request.GET.get('pk', '')

  if request.method == "POST" and pk:
    req = Request.objects.get(pk=pk)
    doctor = Doctor.objects.filter(name = req.doctor)
    if req:
      if not request.POST.get('confirmed'):
        print(request)
        saveRequest(req, request.POST, pk)
      elif request.POST.get('confirmed', 'off') and doctor[0].available:
        saveRequest(req, request.POST, pk)

  if reqs:
    for req in reqs:
      form = {
        'form': RequestApproveForm(instance = req),
        'req': req
      }
      if req.confirmed:
        acceptsForm.append(form)
      else:
        reqsForms.append(form)

    context = {
      'reqsForms': reqsForms,
      'acceptsForm': acceptsForm,
      'doctor': reqs[0].doctor
    }

    return render(request, 'assistant/index.html', context)
  else:
    return render(request, 'assistant/index.html', {})