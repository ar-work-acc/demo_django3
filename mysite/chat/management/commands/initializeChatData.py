import datetime

import pytz
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from chat.models import Message


class Command(BaseCommand):
    help = 'Create initial chat data.'
    company_name = 'meowfish.com'
    users = ['louis_huang', 'alice_moore', 'bob_brown',
             'cathy_jones', 'dean_miller', 'emily_anderson', 'freddy_wilson',
             'george_davis', 'henry_white', 'issac_newton', 'jack_sparrow', 'kevin_chen']

    def handle(self, *args, **options):
        for user in self.users:
            first_name, last_name = user.split('_')
            user, created = User.objects.get_or_create(
                username=user,
                defaults={
                    'first_name': first_name.title(),
                    'last_name': last_name.title(),
                    'email': f'{user}@{self.company_name}',
                    'is_superuser': True,
                    'is_staff': True,
                    'password': make_password('111')
                }
            )
            self.stdout.write(self.style.SUCCESS(f'User ID: {user.id}, created: {created}'))

        alice = User.objects.get(username=self.users[1])
        bob = User.objects.get(username=self.users[2])
        messages = [
            "Hi, Bob! How are you?",
            "Hi, Alice, I'm fine. Thank you.",
            "What are you gonna do today?",
            "I'll just eat and sleep.",
            "Wow, that's a perfect way to waste a great day. If you change your mind, call me.",
            "Sure, maybe later.",
            "You need more exercise...",
            "Okay, let me take a nap first.",
        ]

        for idx, message in enumerate(messages):
            time = datetime.datetime(2022, 2, 6, 18, 0, tzinfo=pytz.UTC) - timezone.timedelta(seconds=(60 - idx))
            if idx % 2 == 0:
                message, created = Message.objects.get_or_create(
                    from_user=alice,
                    to_user=bob,
                    text=messages[idx],
                    created=time,
                )
            else:
                message, created = Message.objects.get_or_create(
                    from_user=bob,
                    to_user=alice,
                    text=messages[idx],
                    created=time,
                )
            self.stdout.write(self.style.SUCCESS(f'Message ID: {message.id}, created: {created}'))
