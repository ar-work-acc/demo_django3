from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.timezone import now

from snippets.models import Snippet


class Command(BaseCommand):
    help = 'Create some snippets with user: meowfish.org@gmail.com'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=1,
            help='number of code snippets to create',
        )

        parser.add_argument(
            '--email',
            type=str,
            default='meowfish.org@gmail.com',
            help='user to associate snippets with.'
        )

    def handle(self, *args, **options):
        count = options['count']
        email = options['email']

        user, created = User.objects.get_or_create(
            username=email,
            defaults={
                'first_name': 'Louis',
                'last_name': 'Huang',
                'email': email,
                'is_superuser': True,
                'is_staff': True,
                'password': make_password('pw20220618')
            }
        )

        self.stdout.write(self.style.SUCCESS(f'User ID: {user.id}, created: {created}'))

        for n in range(count):
            Snippet.objects.create(
                title=f'code title {n}: {now()}',
                owner=user,
                code='console.log("Hi!")',
                language='javascript',
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} snippets.'))
