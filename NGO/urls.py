from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^chat_list/$', views.chat, name='chat_list'),
    url(r'^event_list/$', views.event_all, name='event_list'),
    url(r'^event_details/(?P<id>\d+)/$', views.event_details, name='event_details'),
    url(r'^events_add/$', views.events_add, name='events_add'),
    url(r'^children_list/$', views.children, name='children_all'),    
    url(r'^add_children/$', views.children_add, name='children_add'),
    url(r'^children_detail/(?P<id>\d+)/$', views.children_detail, name='children_detail'),
    url(r'^staff_list/$', views.staff, name='staff_list'),
    url(r'^staff_detail/(?P<id>\d+)/$', views.staff_detail, name='staff_detail'),
    url(r'^donor_list/$', views.donor_list, name='donor_list'),
    url(r'^notification_list/$', views.notification_list, name='notification_list'),
    url(r'^transaction/$', views.transaction, name='transaction'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^edit_children/(?P<id>\d+)/$', views.children_edit, name='edit_children'),

]
