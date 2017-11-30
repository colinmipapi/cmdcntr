from django.conf.urls import include, url

urlpatterns = [
    url(r'^sms/$', phones.views.sms, name="sms"),
    url(r'^ring/$', phones.views.ring, name="ring"),
]
