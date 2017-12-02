from .models import PhoneNumber, Message, Call
from base.models import MyUser

def create_in_call(from_user,to_user):

    call_object = Call(sent_from=from_user)

    call_object.sent_to.add(to_user)

    call_object.save()
