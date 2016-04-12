from django.contrib import admin

from .forms import EventsForm
from .models import Disciplines
from .models import Events
from .models import Members

class EventAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	form = EventsForm

admin.site.register(Disciplines)
admin.site.register(Members)
admin.site.register(Events,EventAdmin)