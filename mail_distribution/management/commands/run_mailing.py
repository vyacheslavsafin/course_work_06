from django.core.management import BaseCommand

from mail_distribution.utils import mail_worker


class Command(BaseCommand):
    def handle(self, *args, **options):
        mail_worker()
