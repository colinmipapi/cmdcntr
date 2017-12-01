from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from base.models import MyUser

class PhoneNumber(models.Model):

    PHONE_TYPE = (
        ("0", "Cell"),
        ("1", "Office"),
        ("2", "Home"),
    )

    user = models.ForeignKey('base.MyUser', related_name='p_user')
    phone = PhoneNumberField(unique=True)
    phone_type = models.CharField(
        max_length=1,
        choices=PHONE_TYPE,
        blank=True,
        null=True,
        )

class Message(models.Model):

    sent_from = models.ForeignKey('base.MyUser', related_name='from_sms')
    sent_to = models.ForeignKey('base.MyUser',  related_name='to_sms')
    text_body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Call(models.Model):

    sent_from = models.ForeignKey('base.MyUser', related_name='from_call')
    sent_to = models.ForeignKey('base.MyUser', related_name='to_call')
