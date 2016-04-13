<<<<<<< HEAD
from datetime import datetime,date,time
from django.core.context_processors import csrf
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import ProfileForm
User = get_user_model()
from .models import Profile, upload_loaction
from sport_event.models import Disciplines,Events,Members
from notifications.signals import notify
from django.shortcuts import redirect
from notifications.models import Notifications
@login_required
def profile_views(request, username):
	user = get_object_or_404(User,username=username)
	profile,created = Profile.objects.get_or_create(user=user)
	requestDisciplines = {}
	if profile.sport_choose:
		for i in profile.sport_choose:
			a = Disciplines.objects.filter(name=i)
			if len(a) != 0:
				requestDisciplines[a[0].name] = a[0].picture.url
	
	profile.organized_match = len(Events.objects.filter(organizer= user))
	profile.save()

	context={
		"profile":profile,
		"requestDisciplines":requestDisciplines,
	}
	return render(request, "profile_view.html",context)
	


@login_required
def edit_profile_views(request):
	user = get_object_or_404(User,username=request.user)
	profile,created = Profile.objects.get_or_create(user=user)
	requestDisciplines = {}
	if request.method == 'POST':
		form = ProfileForm(request.POST,request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return render(request,"dashboard/dashboard.html",{})
	else:
		user = request.user
		profile = user.profile
		form = ProfileForm(instance=profile)
		requestDisciplines = {}
		if profile.sport_choose:
			for i in profile.sport_choose:
				a = Disciplines.objects.filter(name=i)
				if len(a) != 0:
					requestDisciplines[a[0].name] = a[0].picture.url
	context={
		"profile":profile,
		"form":form,
		"title":'Edycja profilu:',
		"requestDisciplines":requestDisciplines,
	}
	return render(request,"profile_edit_view.html",context)


@login_required
def remove_profile_views(request):
	return render(request,"dashboard/remove.html",{})
@login_required
def remove(request):
	user = get_object_or_404(User,username=request.user.username)
	profile,created = Profile.objects.get_or_create(user=user)
	now = datetime.now()
	event = Events.objects.filter(organizer=user,date_event__gte=now.date())

	for i in event:
		for player in i.members.members.all():
			notify.send(
				request.user,
				action = i,
				recipient=player,
				target=i,
				verb='usunal wydarzenie sportowe'
				)

	profile.delete()
	user.delete()
	return redirect('welcome')

@login_required
def dashboard(request):
	try:
		temp = Profile.objects.get(user=request.user)
		print(temp.picture.url)
	except:
		return redirect('edit')

	user = get_object_or_404(User,username=request.user)
	profile,created = Profile.objects.get_or_create(user=user)
	now = datetime.now()

	my_organised_event = user.events_set.filter(date_event=now.date()).order_by('time_event')
	my_event = user.members_set.all()

	my_list_event=[]
	for i in my_event:
		if i.event.date_event==now.date():
			my_list_event.append(i.event)
	
	my_list_event.sort(key = lambda x: x.time_event)


	context = {
				"my_organised_event":my_organised_event,
				"my_event":my_list_event,
				"user":temp,
				}
	return render(request,"dashboard/test.html",context)
=======
from datetime import datetime,date,time

from django.core.context_processors import csrf
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# Create your views here.

from .forms import ProfileForm

User = get_user_model()
from .models import Profile, upload_loaction
from sport_event.models import Disciplines,Events,Members
from notifications.signals import notify

from django.shortcuts import redirect
from notifications.models import Notifications

@login_required
def profile_views(request, username):
	user = get_object_or_404(User,username=username)
	profile,created = Profile.objects.get_or_create(user=user)
	requestDisciplines = {}
	if profile.sport_choose:
		for i in profile.sport_choose:
			a = Disciplines.objects.filter(name=i)
			if len(a) != 0:
				requestDisciplines[a[0].name] = a[0].picture.url
	
	profile.organized_match = len(Events.objects.filter(organizer= user))
	profile.save()

	context={
		"profile":profile,
		"requestDisciplines":requestDisciplines,
	}
	return render(request, "profile_view.html",context)
	


@login_required
def edit_profile_views(request):
	user = get_object_or_404(User,username=request.user)
	profile,created = Profile.objects.get_or_create(user=user)
	requestDisciplines = {}
	if request.method == 'POST':
		form = ProfileForm(request.POST,request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return render(request,"dashboard/dashboard.html",{})
	else:
		user = request.user
		profile = user.profile
		form = ProfileForm(instance=profile)
		requestDisciplines = {}
		if profile.sport_choose:
			for i in profile.sport_choose:
				a = Disciplines.objects.filter(name=i)
				if len(a) != 0:
					requestDisciplines[a[0].name] = a[0].picture.url
	context={
		"profile":profile,
		"form":form,
		"title":'Edycja profilu:',
		"requestDisciplines":requestDisciplines,
	}
	return render(request,"profile_edit_view.html",context)


@login_required
def remove_profile_views(request):
	return render(request,"dashboard/remove.html",{})
@login_required
def remove(request):
	user = get_object_or_404(User,username=request.user.username)
	profile,created = Profile.objects.get_or_create(user=user)
	now = datetime.now()
	event = Events.objects.filter(organizer=user,date_event__gte=now.date())

	for i in event:
		for player in i.members.members.all():
			notify.send(
				request.user,
				action = i,
				recipient=player,
				target=i,
				verb='usunal wydarzenie sportowe'
				)

	profile.delete()
	user.delete()
	return redirect('welcome')

@login_required
def dashboard(request):
	try:
		temp = Profile.objects.get(user=request.user)
		print(temp.picture.url)
	except:
		return redirect('edit')

	user = get_object_or_404(User,username=request.user)
	profile,created = Profile.objects.get_or_create(user=user)
	now = datetime.now()

	my_organised_event = user.events_set.filter(date_event=now.date()).order_by('time_event')
	my_event = user.members_set.all()

	my_list_event=[]
	for i in my_event:
		if i.event.date_event==now.date():
			my_list_event.append(i.event)
	
	my_list_event.sort(key = lambda x: x.time_event)


	context = {
				"my_organised_event":my_organised_event,
				"my_event":my_list_event,
				"user":temp,
				}
	return render(request,"dashboard/dashboard.html",context)
>>>>>>> ce2d6b3e5565e3af6a78e7261f40efc7bd526c7b
