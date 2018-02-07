from django.conf.urls import url
from superadmin import views

app_name = 'superadmin'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^donor_list/$', views.donor_list, name='donor_list'),
    url(r'^donor_detail/(?P<id>\d+)/$', views.donor_detail, name='donor_detail'),
    url(r'^ngo_list/$', views.ngo_list, name='ngo_list'),
    url(r'^ngo_detail/(?P<id>\d+)/$', views.ngo_detail, name='ngo_detail'),
    url(r'^send_detail/$', views.send_detail, name='send_detail'),
    url(r'^transaction_list/$', views.transaction_list, name='transaction_list'),
    url(r'^transaction_detail/(?P<id>\d+)/$', views.transaction_detail, name='transaction_detail'),
    url(r'^notifications/$', views.notification, name='notification'),
    url(r'^notification_detail/$', views.notification_detail, name='notification_detail'),
    url(r'^change_password/$', views.change_password, name='change_password'),

    url(r'^inbox/$', views.inbox, name='inbox'),
    url(r'^send/$', views.send, name='send_message'),
    url(r'^delete/$', views.delete, name='delete_message'),
    url(r'^check/$', views.check, name='check_message'),
    url(r'^(?P<username>[^/]+)/$', views.messages, name='messages'),

]
