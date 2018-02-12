from api.views import login
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^login/$', login),
    url(r'^register/$', views.CreateUserView.as_view(), name='user'),
    url(r'^ngo/$', views.NGOListAPIView.as_view(), name='ngo_api'),
    url(r'^ngo/(?P<pk>\d+)/$', views.NGORetrieveAPIView.as_view(), name='ngo_detail_api'),
    url(r'^children/$', views.ChildrenListAPIView.as_view(), name='children_api'),
    url(r'^children/(?P<pk>\d+)/$', views.ChildrenRetrieveAPIView.as_view(), name='children_detail_api'),
    url(r'^events/$', views.EventListAPIView.as_view(), name='event_api'),
    url(r'^events/(?P<pk>\d+)/$', views.EventRetrieveAPIView.as_view(), name='event_detail_api'),
    url(r'^events-new/$', views.EventCreateView.as_view(), name='event_create_api'),
    url(r'^donor/$', views.DonorRudAPIView.as_view(), name='donor_api'),
    url(r'^donor/(?P<pk>\d+)/$', views.DonorRetrieveRudAPIView.as_view(), name='donor_detail'),
    url(r'^donor-new/$', views.DonorCreateView.as_view(), name='donor_create_api'),

]
