from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):

    source = models.CharField(max_length=500, blank=True, null=True)
