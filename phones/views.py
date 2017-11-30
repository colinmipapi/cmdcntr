from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


from django_twilio.decorators import twilio_view
from twilio.twiml.messaging_response import MessagingResponse

@twilio_view
def sms(request):

    r = MessagingResponse()
    r.message('Hello from your Django app!')

    return r
