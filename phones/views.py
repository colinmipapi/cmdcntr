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

@twilio_view
def incoming_call(request):

    from_number = request.values.get('From', None)

    resp = VoiceResponse()
    resp.say("Hey there")
    #resp.play()
    g = Gather(numDigits=1, action="/handle-key", method="POST")
    g.say("To give me a call, press 1. Press any other key to start over.")
    resp.append(g)

    return str(resp)

@twilio_view
def handle_key(request):
    """Handle key press from a user."""

    # Get the digit pressed by the user
    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":
        resp = VoiceResponse()

        resp.dial("+15166407250")
        # If the dial fails:
        resp.say("The call failed, or the remote party hung up. Goodbye.")

        return str(resp)
