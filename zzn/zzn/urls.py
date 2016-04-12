from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'zzn.views.home', name='welcome'),
    # url(r'^$', TemplateView.as_view(template_name='welcome.html'), name='welcome'),
    
    #profile
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^profile/edit/$','profiles.views.edit_profile_views',name='edit'),
    url(r'^profile/remove/$','profiles.views.remove_profile_views',name='remove_profile_views'),
    url(r'^profile/remove2/$','profiles.views.remove',name='remove_profile_views2'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$','profiles.views.profile_views',name='profile'),
    

    #dashboard
    url(r'^dashboard/$','profiles.views.dashboard',name='dashboard'),

    
    #events
    url(r'^add_env/$','sport_event.views.add_new_sport_env',name='spoort_env'),
    url(r'^find_env/$','sport_event.views.find_sport_env',name='find_sport_env'),
    url(r'^event/(?P<id>\d+)/$','sport_event.views.sport_env_detail',name='sport_detail'),
    url(r'^your_event/$','sport_event.views.your_event',name='your_event'),
    url(r'^event/edit/(?P<id>\d+)/$','sport_event.views.sport_env_edit',name='event_edit'),
    url(r'^event/remove/(?P<id>\d+)/$','sport_event.views.sport_env_remove',name='event_remove'),

    #AJAX
    url(r'^ajax_event/(?P<id>\d+)/$','sport_event.views.ajax_event',name='ajax_event'),
    url(r'^ajax_eventReady/(?P<id>\d+)/$','sport_event.views.ajax_eventReady',name='ajax_eventReady'),


    #Notifications
    url(r'^notifications/$','notifications.views.all',name='notifications_all'),
    url(r'^notifications/delete$','notifications.views.notifications_delete',name='notifications_delete'),
    # url(r'^notifications/unread/$','notifications.views.unread',name='notifications_unread'),
    url(r'^notifications/(?P<id>\d+)/$','notifications.views.read',name='notifications_read'),
    url(r'^notifications/ajax/$', 'notifications.views.get_notifications_ajax', name='get_notifications_ajax'),

)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)