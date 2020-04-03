from django import forms
from patient.models import Request, Patient

class RequestForm(forms.ModelForm):
  class Meta:
    model = Request
    fields = ["doctor"]

class PatientForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = ['fullname', 'dob', 'age', 'gender', 'picture']