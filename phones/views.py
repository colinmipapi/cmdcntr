from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import Gather, VoiceResponse, Say

def load_twilio_config():
    twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    twilio_number = os.environ.get('TWILIO_NUMBER')

    if not all([twilio_account_sid, twilio_auth_token, twilio_number]):
        logger.error(NOT_CONFIGURED_MESSAGE)
        raise MiddlewareNotUsed

    return (twilio_number, twilio_account_sid, twilio_auth_token)


@csrf_exempt
def sms_response(request,msg):
    r = MessagingResponse()
    r.message(msg)
    return HttpResponse(str(r))

@csrf_exempt
def ring_in(request):

    from_number = request.POST.get('From', '')

    resp = VoiceResponse()
    resp.say("Hey there")
    #resp.play()
    g = Gather(numDigits=1, action="/handle-key", method="POST")
    g.say("To give me a call, press 1. Press any other key to start over.")
    resp.append(g)

    return HttpResponse(str(resp))


@csrf_exempt
def handle_key():
    """Handle key press from a user."""

    # Get the digit pressed by the user
    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":
        resp = VoiceResponse()

        resp.dial("+15166407250")
        # If the dial fails:
        resp.say("The call failed, or the remote party hung up. Goodbye.")

        return HttpResponse(str(resp))
