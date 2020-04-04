from django import forms
# model
from patient.models import Request

class RequestApproveForm(forms.ModelForm):
  class Meta:
    model = Request
    fields = ["confirmed"]
    # fields = "__all__"

    
