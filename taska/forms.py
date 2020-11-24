from django.forms import ModelForm
from django import forms
from.models import items

class todoform(forms.ModelForm):
    class Meta:
        model=items
        fields=['TEXT']