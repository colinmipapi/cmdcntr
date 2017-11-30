from django.conf.urls import include, url

urlpatterns = [
    url(r'^sms/$', 'phones.views.sms'),
    url(r'^ring/$', 'phones.views.ring'),
]
