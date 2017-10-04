from __future__ import print_function
import os
import json
from django.core.management.base import BaseCommand, CommandError
from collections import namedtuple
from django.contrib.auth.models import User
from account.models import Account
from portal.core.fit import models
from portal.core.fit import calc


class Command(BaseCommand):
    help = 'Brutally Set Account Defaults'
     
    def handle(self, *args, **options):
        for u in User.objects.all():
            a = Account.objects.get(user=u)
            a.timezone = 'America/Denver'
            a.language = 'en'
            a.save()

