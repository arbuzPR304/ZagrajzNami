from django import forms
from .models import Profile
from django.forms import ModelForm, Textarea
from django.core.exceptions import ValidationError
from django_cleanup.signals import cleanup_pre_delete, cleanup_post_delete

class ProfileForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)

		self.fields['location'].label = "Lokalizacja"
		self.fields['picture'].label = "Foto"
		self.fields['about_player'].label = "O mnie"
		self.fields['sport_choose'].label = "Ulubione dyscypliny"


	class Meta:
		model = Profile
		fields = ['location','picture','about_player','sport_choose']
		widgets = {'about_player': Textarea(attrs={'cols': 30, 'rows': 5}),}

	def sorl_delete(**kwargs):
		delete(kwargs['file'])

	
