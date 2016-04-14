import os

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


from allauth.socialaccount.models import SocialAccount
from multiselectfield import MultiSelectField


def upload_location(instance,filename):
	location = str(instance.user.username)
	filename, file_extension = os.path.splitext(filename)
	return "%s/%s%s" %(location,"photo",file_extension)


class Profile(models.Model):
	user = models.OneToOneField(User)
	location = models.CharField(default="Opole", max_length=120, null=True, blank=True)
	picture = models.ImageField(upload_to=upload_location, null=False, blank=False)
	played_match = models.IntegerField(default=0,null=True,blank=True)
	organized_match = models.IntegerField(default=0,null=True,blank=True)
	about_player = models.CharField(max_length=5000, null=False, blank=True)
	sports =(
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
	)
	sport_choose = MultiSelectField(choices=sports,blank=True,null=False,
	 max_choices=4,max_length=500)


	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		url = reverse("profile",kwargs={"username":self.user.username})
		return url


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])