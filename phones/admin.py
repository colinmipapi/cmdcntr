from django.contrib import admin
from .models import PhoneNumber, Message, Call
# Register your models here.

admin.site.register(PhoneNumber)
admin.site.register(Message)
admin.site.register(Call)
