from django import forms
from teamapp.models import Team

class teamform(forms.ModelForm):
	class Meta:
		model=Team
		fields="__all__"