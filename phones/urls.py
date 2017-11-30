from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^sms_response/$', views.sms_response, name="sms_response"),
    url(r'^ring_in/$', views.ring_in, name="ring_in"),
]
