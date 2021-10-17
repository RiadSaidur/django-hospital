from django import forms
from patient.models import Request, Patient

class RequestForm(forms.ModelForm):
  class Meta:
    model = Request
    fields = ["doctor"]

class PatientForm(forms.ModelForm):
  dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

  class Meta:
    model = Patient
    fields = ['fullname', 'dob', 'currentState', 'gender', 'picture']