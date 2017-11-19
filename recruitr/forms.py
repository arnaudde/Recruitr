from django import forms
from django.forms import extras
from .models import Schedule


class ScheduleForm(forms.Form):
    datetime_begin = forms.DateTimeField()
    datetime_end = forms.DateTimeField()


class RecruiterForm(forms.Form):
	def __init__(self,*args,**kwargs):
		choices = kwargs.pop("choices")
		super(RecruiterForm, self).__init__(*args, **kwargs)
		self.fields['id_recruiter'].choices=choices
	id_recruiter=forms.ChoiceField(choices=[(1,1),(2,2)])