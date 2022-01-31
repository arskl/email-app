from django import forms
from django.forms import ModelForm

from .models import *


class EmailForm(forms.ModelForm):
	class Meta:
		model = Email
		fields = ['email_field']
