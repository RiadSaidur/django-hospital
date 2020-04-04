from django.shortcuts import render
# decorators
from django.contrib.auth.decorators import login_required
from assistant.decorators import assistant_only
# models
from patient.models import Request, Appointment
# date-time
from django.utils import timezone
# forms
from assistant.forms import RequestApproveForm

@login_required
@assistant_only
def index(request):
  reqs = Request.objects.filter(confirmed = False, created_at__date__gte = timezone.now().date()).order_by('created_at')
  accepts = Request.objects.filter(confirmed = True, created_at__date__gte = timezone.now().date()).order_by('created_at')

  # forms = []

  # for req in reqs:
  #   if request.method == 'POST':
  #     form = 
  #   collection = {
  #     'req': req,
  #     'form': 
  #   }
  #   forms.append(req.doctor)

  # print(forms)

  if request.method == 'POST':
    print(request.POST)
  
  context = {
    'reqs': reqs,
    'accepts': accepts,
    'doctor': reqs[0].doctor
  }

  return render(request, 'assistant/index.html', context)