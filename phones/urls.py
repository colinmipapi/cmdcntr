from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^sms_response/$', views.sms_response, name="sms_response"),
    url(r'^ring/$', views.ring_in, name="ring_in"),
    url(r'^ring/handle_key/$', views.handle_key, name="handle_key"),
    url(r'^ring/handle_recording/$', views.handle_recording, name="handle_recording"),
]
