from django.db import models

class Group(models.Model):

    title = models.CharField(max_length=500)

class Contact(models.Model):

    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name="group_contacts")
    source = models.CharField(max_length=500, blank=True, null=True)
    date_created = models.DateTimeField(null=True, blank=True)
