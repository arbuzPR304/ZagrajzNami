from django.contrib import admin
# Register your models here.

from .models import Profile
from .forms import ProfileForm

class ProfileAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	form = ProfileForm
		
admin.site.register(Profile,ProfileAdmin)
