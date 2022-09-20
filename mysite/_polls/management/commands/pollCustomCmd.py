from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Just a sample, does nothing.
    Usage:
     ./manage.py pollCustomCmd --help
    ./manage.py pollCustomCmd 1 2 3 --delete
    ./manage.py pollCustomCmd 1 2 3
    """
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)
        parser.add_argument(
            '--delete',
            action='store_true',  # default = False (the opposite)
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        print('### Poll IDs ###:')
        for poll_id in options['poll_ids']:
            print(poll_id)
        print("### ----- ###")
        print(f"delete option: {options['delete']}")
        self.stdout.write(self.style.SUCCESS(f'Successfully closed poll {poll_id}'))
