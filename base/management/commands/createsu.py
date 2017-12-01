from django.core.management.base import BaseCommand
from base.models import MyUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not MyUser.objects.filter(username="colin").exists():
            MyUser.objects.create_superuser("colin", "cjm@colinmcfaul.com", "admin")
