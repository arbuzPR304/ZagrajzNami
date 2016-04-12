# -*- coding: utf-8 -*-
from datetime import datetime,date,time

from django.core.context_processors import csrf
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404,redirect, Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import EventsForm,FindForm
from .models import Events,Disciplines,Members
from profiles.models import Profile
from comments.forms import CommentForm
from comments.models import Comment
from notifications.signals import notify


from datetime import datetime,date,time
User = get_user_model()

@login_required
def add_new_sport_env(request):
	try:
		temp = Profile.objects.get(user=request.user)
		a = temp.picture.url
	except:
		return redirect('edit')
	if request.method == 'POST':
		form = EventsForm(request.POST)
		if form.is_valid():
			env = form.save(commit=False)
			env.organizer = request.user
			env.save()
			players = Members(event=env)
			players.save()
			players.members.add(request.user)
			players.save()
			return redirect('dashboard')
	else:
		form = EventsForm()
	context={
		"form":form,
		"title":"Dodaj wydarzenie:"
	}
	return render(request,"event\create_event.html",context)


@login_required
def find_sport_env(request):
	try:
		temp = Profile.objects.get(user=request.user)
		a = temp.picture.url
	except:
		return redirect('edit')

	if request.method == 'POST':
		form = FindForm(request.POST)
		if form.is_valid():
			dataRequest = form.cleaned_data

			temp_disc = Disciplines.objects.filter(name=dataRequest["Disciplines"])
			date_time = form.cleaned_data["dateOne"]
			date_time2 = form.cleaned_data["dateTwo"]

			datestr=datetime.strptime( date_time, "%Y-%m-%d" )
			datestr2=datetime.strptime( date_time2, "%Y-%m-%d" )


			results = Events.objects.filter(profession_choose=temp_disc,city = form.cleaned_data["city"],
				date_event__gte=datestr,date_event__lte=datestr2).order_by('date_event', 'time_event')
			context = {
				"results":results,
				"title2": dataRequest['Disciplines']+" - "+form.cleaned_data["city"],
			}
			return render(request,"event\ind_event_map.html",context)

	else:
		form = FindForm()
	context={
		"form":form,
		"title":"Szukaj wydarzenia:"
	}
	return render(request,"event\ind_event.html",context)

@login_required
def sport_env_detail(request, id):
	try:
		temp = Profile.objects.get(user=request.user)
		a = temp.picture.url
	except:
		return redirect('edit')

	event = Events.objects.get(id=id)
	profile = Profile.objects.get(user = event.organizer)

	comments = event.comment_set.all()
	if len(comments)<30:
		comment_form = CommentForm(request.POST or None)
		if comment_form.is_valid():
			comment_text = comment_form.cleaned_data['tekst']
			new_comment = Comment.objects.create_comment(
					user=request.user, 
					path=request.get_full_path(), 
					text=comment_text,
					event = event,)
			# notify.send(
			# 	request.user,
			# 	action = new_comment,
			# 	recipient=event.organizer,
			# 	target=new_comment.event,
			# 	verb='dodal nowy komentarz do wydarzenia'
			# 	)
			for player in event.members.members.all():
				notify.send(
					request.user,
					action = new_comment,
					recipient=player,
					target=new_comment.event,
					verb='dodal nowy komentarz do wydarzenia'
				)
			return HttpResponseRedirect(event.get_absolute_url())
	else:
		comment_form=None
	context ={
		"event":event,
		"profile":profile,
		"comments":comments,
		"comment_form":comment_form
	}
	return render(request,"event\detail_event.html",context)
	# except:
	# 	raise Http404

@login_required
def ajax_event(request, id):
	if request.is_ajax():
		ajaxList = {}
		event = Events.objects.get(id=id)
		
		date_event =event.date_event
		time_event =event.time_event

		a = date_event.strftime("%Y-%m-%d")
		b = time_event.strftime("%H:%M:%S")

		datestr=datetime.strptime( a+"T"+b, "%Y-%m-%dT%H:%M:%S" )
		now = datetime.now()


		zawodnicy = Members.objects.get(event=event)
		
		if not( request.user in zawodnicy.members.all()):
			zawodnicy.members.add(request.user)
			zawodnicy.save()
		else:
			zawodnicy.members.remove(request.user)
			zawodnicy.save()
		counter = 1
		
		event = Events.objects.get(id=id)
		zawodnicy = Members.objects.get(event=event)
		for i in zawodnicy.members.all():
			temp = Profile.objects.get(user=i)
			ajaxList["user"+str(counter)]=[str(temp.user.username),str(temp.get_absolute_url()),str(temp.picture.url)]
			counter=counter+1

		ajaxDict = {}
		ajaxDict["user"] = ajaxList


		zawodnicy = zawodnicy.members.all()
		freePlace = event.max_number_of_player-len(zawodnicy)
		if freePlace<0:
			freePlace=0

		howPlayers = len(zawodnicy)

		buttonStr=buttonInfo=""
	

	if datestr>now:
		if not(request.user in zawodnicy) and freePlace ==0:
			buttonStr="Wszytkie miesjca zapelnione"
			buttonInfo=None
		elif not(request.user in zawodnicy) and freePlace>0:
			buttonStr = "Zagraj"
			buttonInfo = "success"
		else:
			buttonStr = "Nie gram"
			buttonInfo = "warning"

		ajaxDict["element"]  = {
			"freePlace":freePlace,
			"howPlayers":howPlayers,
			"buttonStr":buttonStr,
			"buttonInfo":buttonInfo,
		}

		return JsonResponse(ajaxDict)
	else:
		raise Http404
@login_required
def ajax_eventReady(request, id):
	if request.is_ajax():
		event = Events.objects.get(id=id)

		date_event =event.date_event
		time_event =event.time_event

		a = date_event.strftime("%Y-%m-%d")
		b = time_event.strftime("%H:%M:%S")

		datestr=datetime.strptime( a+"T"+b, "%Y-%m-%dT%H:%M:%S" )
		now = datetime.now()

		zawodnicy = Members.objects.get(event=event)
		ajaxList = {}
		counter = 1
		for i in zawodnicy.members.all():
			temp = Profile.objects.get(user=i)
			ajaxList["user"+str(counter)]=[str(temp.user.username),str(temp.get_absolute_url()),str(temp.picture.url)]
			counter=counter+1
		ajaxDict = {}
		ajaxDict["user"] = ajaxList



		zawodnicy = zawodnicy.members.all()
		freePlace = event.max_number_of_player-len(zawodnicy)
		if freePlace<0:
			freePlace=0

		howPlayers = len(zawodnicy)

		buttonStr=buttonInfo=""
		
		if datestr>now:
			if not(request.user in zawodnicy) and freePlace ==0:
				buttonStr="Wszytkie miesjca zapelnione"
				buttonInfo=None
			elif not(request.user in zawodnicy) and freePlace>0:
				buttonStr = "Zagraj"
				buttonInfo = "success"
			else:
				buttonStr = "Nie gram"
				buttonInfo = "warning"
		else:
			buttonStr="Zapis niemożliwy, termin gry zakończony"
			buttonInfo=None

		ajaxDict["element"]  = {
			"freePlace":freePlace,
			"howPlayers":howPlayers,
			"buttonStr":buttonStr,
			"buttonInfo":buttonInfo,
		}
		return JsonResponse(ajaxDict)

	else:
		raise Http404	

@login_required
def your_event(request):
	user = get_object_or_404(User,username=request.user)
	profile,created = Profile.objects.get_or_create(user=user)
	now = datetime.now()

	my_organised_event = user.events_set.filter(date_event__gte=now.date())
	my_event = user.members_set.all()
	
	my_list_event=[]
	for i in my_event:
		if i.event.date_event>=now.date():
			my_list_event.append(i.event)
	
	my_list_event.sort(key = lambda x: x.date_event)

	context ={
		"my_organised_event":my_organised_event,
		"my_event":my_list_event,
		"title":"Twoje wydarzenia",
	}
	
	return render(request,"event\your_event.html",context)

@login_required
def sport_env_edit(request,id):
	try:
		event = get_object_or_404(Events,organizer=request.user,pk=id)
		if request.POST:
		    form = EventsForm(request.POST, instance=event)
		    if form.is_valid():
		        form.save()
		        for player in event.members.members.all():
		        	notify.send(
		        		request.user,
		        		action = event,
		        		recipient=player,
		        		target=event,
		        		verb='dokonal edycji wydarzenia'
		        		)
		        return redirect("your_event")
		else:
		    form = EventsForm(instance=event)

		context ={
		"title":"Edycja",
		"event":event,
		"form":form,
		}
		return render(request,"event\edit.html",context)
	except:
		raise Http404

@login_required
def sport_env_remove(request,id):
	try:
		event = get_object_or_404(Events,organizer=request.user,pk=id)
		for player in event.members.members.all():
			notify.send(
        		request.user,
        		action = event,
        		recipient=player,
        		target=event,
        		verb='Usunieto wydarzenie'
		    )
		members = get_object_or_404(Members,event=event)
		members.delete()
		event.delete()

		return redirect("your_event")
	except:
		raise Http404

