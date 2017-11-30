from django.conf.urls import include, url

url_pattern = [
    url(r'^sms/$', 'phones.views.sms'),
    url(r'^ring/$', 'phones.views.ring'),
]
