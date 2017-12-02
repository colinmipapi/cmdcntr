from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import PhoneNumber, Message, Call

from .run import load_twilio_config
from .backends import create_in_call

from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import Gather, VoiceResponse, Say, Dial

@csrf_exempt
def sms_response(request,msg):
    r = MessagingResponse()
    r.message(msg)
    return HttpResponse(str(r))

@csrf_exempt
def ring_in(request):

    from_number = request.POST.get('From', '')

    resp = VoiceResponse()

    from_phone_object = PhoneNumber.objects.get_or_create(phone=from_number)

    if from_phone_object[1] == False:

        from_user = from_phone_object[0].user
        first_name = from_user.first_name

        if first_name != None:
            resp.say("Hey %s..." % first_name)
        else:
            resp.say("Hey there...")

    else:

        from_user = MyUser(username="from_number",active=True)
        from_user.active = True
        from_user.save()

        from_phone_object[0].user = from_user

        resp.say("Hey there...")

    #resp.play()
    g = Gather(num_digits=1, action="/phone/ring/handle_key/", method="POST")
    g.say("Thanks for calling Colin... press 1 to give him a call... press 2 to leave a voicemail... and press any other key to start over.")
    resp.append(g)

    to_user = MyUser.objects.get(username="colin",first_name="Colin",last_name="McFaul")

    create_in_call(from_user,to_user)

    return HttpResponse(str(resp))


@csrf_exempt
def handle_key(request):
    """Handle key press from a user."""

    # Get the digit pressed by the user
    digit_pressed = request.POST.get('Digits','')
    if digit_pressed == "1":

        resp = VoiceResponse()
        dial = Dial()
        dial.number('516-640-7250')
        resp.append(dial)

        return HttpResponse(str(resp))

    elif digit_pressed == "2":

        resp = VoiceResponse()
        resp.say("Record your message after the tone.")
        resp.record(maxLength="30", action="/phone/ring/handle_recording/")
        return HttpResponse(str(resp))

@csrf_exempt
def handle_recording(request):

    recording_url = request.values.get("RecordingUrl", None)

    resp = VoiceResponse()
    resp.say("Thanks for leaving a message... take a listen to what you said.")
    resp.play(recording_url)
    resp.say("Goodbye.")
    return HttpResponse(str(resp))
