import datetime
from django.utils import timezone
from mail_distribution.models import *


def mail_sender():
    sending_list = MailDistribution.objects.all()
    for obj in sending_list:
        now = datetime.datetime.now()
        now = timezone.make_aware(now, timezone.get_current_timezone())

