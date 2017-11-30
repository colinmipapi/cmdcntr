from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^sms/$', views.sms, name="sms"),
    url(r'^ring/$', views.ring, name="ring"),
]
