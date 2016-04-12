# -*- coding: utf-8 -*
import datetime
from datetime import datetime,date,time

#created
from profiles.models import Profile
#django
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

#instaled
from durationfield.db.models.fields.duration import DurationField

def upload_loaction(instance,filename):
    location = str(instance.name)
    return "%s/%s" %(location,filename)

class Disciplines(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    picture = models.ImageField(upload_to=upload_loaction, null=True, blank=True)
    

    def __str__(self):
        return self.name

class Events(models.Model):
    # general
    title = models.CharField(max_length=120, blank=False, null=True, verbose_name = 'Nazwa')
    organizer = models.ForeignKey(User,verbose_name='Organizator')
    profession_choose = models.ForeignKey(Disciplines,verbose_name='Dyscyplina')
    max_number_of_player = models.PositiveSmallIntegerField(blank=False, null=True, verbose_name= 'Maksymalna liczna graczy')
    # address
    number_street = models.PositiveSmallIntegerField(blank=False, null=True,verbose_name='Numer')
    address = models.CharField(max_length=120, blank=False, null=True,verbose_name='Ulica')
    city = models.CharField(max_length=120, blank=False, null=True,verbose_name='Miasto')
    latlong = models.CharField(max_length=120, blank=False, null=True,verbose_name='Dlugosc, szerokosc')
    #organise
    time_event = models.TimeField(blank=False, null=True, verbose_name='Czas wydarzenia')
    date_event = models.DateField(blank=False, null=True, verbose_name='Data wydarzenia')
    duration = models.TimeField(blank=False, null=True,verbose_name='Czas trwania')
    rules = models.CharField(max_length=500,blank=True,verbose_name='Od organizatora')
    created_at = models.DateTimeField(default=datetime.now,auto_now_add=True)
    players = models.ManyToManyField(User,related_name='players')
    
    class Meta:
        ordering = ['date_event']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("sport_detail", kwargs={"id":self.id})
    
    def is_past_due(self):
        date_event =self.date_event
        time_event =self.time_event
        a = date_event.strftime("%Y-%m-%d")
        b = time_event.strftime("%H:%M:%S")
        datestr=datetime.strptime( a+"T"+b, "%Y-%m-%dT%H:%M:%S" )
        now = datetime.now()
        if now > datestr:
            return True
        return False


class Members(models.Model):
    event = models.OneToOneField(Events,primary_key=True)
    members = models.ManyToManyField(User)

    def __str__(self):
        return str(self.event)

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
