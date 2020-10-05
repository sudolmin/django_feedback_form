from .models import Answer
from django import forms

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['Descibe','Rate']
		widgets={
			'Descibe': forms.Textarea(attrs={'class':'input', 
			'placeholder':'Descibe your views',
			'rows':2}
			),
		}