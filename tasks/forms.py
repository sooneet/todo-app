from turtle import title
from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter item'}))
	
	class Meta:
		model = Task
		fields = '__all__'
