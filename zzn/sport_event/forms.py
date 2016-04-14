from django import forms
from .models import Events,Disciplines
from django.forms import ModelForm, Textarea,DateInput,TimeInput
from time import gmtime, strftime
from datetime import datetime,date,time
from django.forms.extras.widgets import SelectDateWidget

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'

class EventsForm(forms.ModelForm):

	class Meta:
	        model = Events
	        exclude = ['organizer','players','address','number_street']
	        widgets = {'rules': Textarea(attrs={'cols': 30, 'rows': 10}),
	        			'date_event':DateInput(),
	        			'time_event':TimeInput(),
	        			'duration':TimeInput(),
	        			}
	def clean_max_number_of_player(self):
		max_number_of_player = self.cleaned_data.get('max_number_of_player')
		if max_number_of_player<=1:
			raise forms.ValidationError("Podaj liczbę wieksza od 1")
		elif max_number_of_player>30:
			raise forms.ValidationError("Podaj liczbę mniejszą niz 30")
		return max_number_of_player

	def clean_date_event(self):
		date_event =self.cleaned_data.get('date_event')
		time_event =self.cleaned_data.get('time_event')
		if time_event:
			a = date_event.strftime("%Y-%m-%d")
			b = time_event.strftime("%H:%M:%S")
			datestr=datetime.strptime( a+"T"+b, "%Y-%m-%dT%H:%M:%S" )
			now = datetime.now()
			if now>datestr:
				raise forms.ValidationError("Podaj przyszłą datę")
		else:
			raise forms.ValidationError("Podaj godzinę")
		return date_event

	def clean_city(self):
		city =self.cleaned_data.get('city')
		city = city.capitalize()
		return city

class FindForm(forms.Form):
	def choose():
		list = [
		('American Football','American Football'),
        ('Badminton','Badminton'),
        ('Futsal','Futsal'),
        ('Hokej na lodzie','Hokej na lodzie'),
        ('Koszykówka','Koszykówka'),
        ('Kręgle','Kręgle'),
        ('Paintball','Paintball'),
        ('Piłka nożna','Piłka nożna'),
        ('Piłka ręczna','Piłka ręczna'),
        ('Siatkówka','Siatkówka'),
        ('Siatkówka plażowa','Siatkówka plażowa'),
        ('Szachy','Szachy'),
        ('Tenis','Tenis')
        ]
		return list

	Disciplines = forms.ChoiceField(widget = forms.Select(), 
                 choices = choose(),required = True,label="Dyscyplina")
	city = forms.CharField(max_length=100,label="Miasto",required = True)
	dateOne = forms.CharField(widget = DateInput(),label="Podaj przedział dni, rozpoczęcie",required=True)
	dateTwo = forms.CharField(widget = DateInput(),label="Podaj przedział dni, zakończenie",required=True)
	
	def clean_city(self):
		city =self.cleaned_data.get('city')
		city = city.capitalize()
		return city
