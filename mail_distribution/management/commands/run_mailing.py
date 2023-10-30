from django.core.management import BaseCommand

from mail_distribution.utils import mail_sender


class Command(BaseCommand):
    def handle(self, *args, **options):
        mail_sender()
