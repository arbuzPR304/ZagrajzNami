import json

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, Http404, HttpResponseRedirect, redirect, get_object_or_404

from .models import Notifications

@login_required
def all(request):

	notifications = Notifications.objects.all_for_user(request.user).order_by("read")
	context = {
		"notifications": notifications,
		"title": "Powiadomienia"
	}

	return render(request,"notifications/all.html",context)


@login_required
def read(request, id):
	try:
		next=request.GET.get('next',None)
		notifications = Notifications.objects.get(id=id)
		if notifications.recipient == request.user:
			notifications.read = True
			notifications.save()
			if next is not None:
				return HttpResponseRedirect(next)
			else:
				return HttpResponseRedirect(reverse("notifications_all"))
		else:
			raise Http404
	except:
		raise HttpResponseRedirect(reverse("notifications_all"))
@login_required
def get_notifications_ajax(request):
	notifications = Notifications.objects.all_for_user(request.user).recent()
	count = notifications.count()
	notes = []
	for note in notifications:
		notes.append(str(note.get_link))
	data = {
		"notifications":notes,
		"count":count,
	}
	json_data=json.dumps(data)
	return HttpResponse(json_data,content_type='applicaton/json')

@login_required
def notifications_delete(request):
	notifications = Notifications.objects.all_for_user(request.user)
	for i in notifications:
		i.delete()
	return redirect("notifications_all")