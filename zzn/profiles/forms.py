from django import forms
from .models import Profile
from django.forms import ModelForm, Textarea
from django.core.exceptions import ValidationError
from django_cleanup.signals import cleanup_pre_delete, cleanup_post_delete
from django.core.files.images import get_image_dimensions
from django.db.models.fields.files import ImageFieldFile

class ProfileForm(forms.ModelForm):

	pictureMaxWidth = 500
	pictureMaxHeight = 500
	pictureMaxSizeInKB = 128 
	validImageTypes = [
		"image/jpg",
		"image/jpeg",
		"image/png",
		"image/gif",
	]

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['location'].label = "Lokalizacja"
		self.fields['picture'].label = "Foto (maksymalny rozmiar: 500x500px, rozmiar 128kB)"
		self.fields['about_player'].label = "O mnie"
		self.fields['sport_choose'].label = "Ulubione dyscypliny"


	class Meta:
		model = Profile
		fields = ['location','picture','about_player','sport_choose']
		widgets = {'about_player': Textarea(attrs={'cols': 30, 'rows': 5}),}

	def sorl_delete(**kwargs):
		delete(kwargs['file'])

	# http://stackoverflow.com/a/1875453
	def clean_picture(self):
		
		picture = self.cleaned_data.get('picture')

		# czy obraz został faktycznie przesłany w formularzu bezpośrendio przez użytkownika, a nie przez domyślną wartość
		if type(picture) is ImageFieldFile:
			return picture

		if picture:
			if any([picture.content_type == e for e in self.validImageTypes]) == False:
				raise forms.ValidationError("Nie podano prawidłowego pliku")
			if picture.size > self.pictureMaxSizeInKB*1024:
				raise forms.ValidationError("Podany obraz przekracza dopuszczalny rozmiar (przesłany rozmiar: "+str(round(float(picture.size)/1024))+"kB)")
			w, h = get_image_dimensions(picture)
			if w > self.pictureMaxWidth or h > self.pictureMaxHeight:
				raise forms.ValidationError("Rozmiary przesłanego obrazu są za duże!")	
			return picture
		else:
			raise forms.ValidationError("Podaj właściwy obraz")


	
