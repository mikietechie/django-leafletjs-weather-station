'''
Copyrights 2021
Work Done By Mike Zinyoni https://github.com/mikietechie
mzinyoni7@gmail.com (Do not spam please)
(Open to work)
'''

from django.core.management.base import BaseCommand, CommandError
from app.models import Location


class Command(BaseCommand):
    help = 'Setup locations other fields'

    def handle(self, *args, **options):
        try:
            for location in Location.objects.all():
                location.save()
        except Exception as e:
            raise CommandError(str(e))
        self.stdout.write(self.style.SUCCESS("Initial locations ready!!!"))