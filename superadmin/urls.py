from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^donor_list/$', views.donor_list, name='donor_list'),
    url(r'^donor_detail/$', views.donor_detail, name='donor_detail'),
    url(r'^ngo_list/$', views.ngo_list, name='ngo_list'),
    url(r'^ngo_detail/(?P<id>\d+)/$', views.ngo_detail, name='ngo_detail'),
    url(r'^send_detail/$', views.send_detail, name='send_detail'),
    url(r'^transaction_list/$', views.transaction_list, name='transaction_list'),
    url(r'^transaction_detail/(?P<id>\d+)/$', views.transaction_detail, name='transaction_detail'),
    url(r'^notifications/$', views.notification, name='notification'),
    url(r'^change_password/$', views.change_password, name='change_password'),

]
