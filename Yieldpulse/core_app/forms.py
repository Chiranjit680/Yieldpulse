from django import forms
from .models import *

class Signin(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'