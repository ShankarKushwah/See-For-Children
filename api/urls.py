from api.views import login
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^login/$', login),
    url(r'^register/$', views.CreateUserView.as_view(), name='user'),
    url(r'^ngo/$', views.NGOListAPIView.as_view(), name='ngo_list'),
    url(r'^ngo/(?P<pk>\d+)/$', views.NGORetrieveAPIView.as_view(), name='ngo_detail_api'),

]
