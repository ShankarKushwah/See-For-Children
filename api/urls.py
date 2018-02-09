from api.views import login
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^login/$', login),
    url(r'^register/$', views.CreateUserView.as_view(), name='user'),
]
