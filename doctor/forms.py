from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from doctor.models import Request, Patient

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class RequestForm(forms.ModelForm):
  class Meta:
    model = Request
    fields = ["doctor"]

class PatientForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = ['fullname', 'dob', 'age', 'gender']