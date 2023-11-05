import datetime

from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from mail_distribution.models import *


def mail_worker():
    sending_list = MailDistribution.objects.all()
    for obj in sending_list:
        if obj.is_active:
            now = datetime.datetime.now()
            now = timezone.make_aware(now, timezone.get_current_timezone())
            if obj.status == constants.MAILING_CREATED:
                if obj.time_start <= now:
                    obj.time_start = now
                    obj.status = constants.MAILING_ACTIVE
                    obj.save()
            if obj.status == constants.MAILING_ACTIVE:
                if obj.time_end <= now:
                    obj.status = constants.MAILING_FINISHED
                    obj.save()
                elif obj.time_next <= now:
                    mail_sender(obj)
                    if obj.frequency == constants.DAILY:
                        obj.time_next = now + datetime.timedelta(days=1)
                    elif obj.frequency == constants.WEEKLY:
                        obj.time_next = now + datetime.timedelta(days=7)
                    elif obj.frequency == constants.MONTHLY:
                        obj.time_next = now + datetime.timedelta(days=30)
                    obj.save()


def mail_sender(obj: MailDistribution):
    for client in obj.clients.all():
        mail_status = send_mail(
            subject=obj.message.title,
            message=obj.message.body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[client.email]
        )
        now = datetime.datetime.now()
        now = timezone.make_aware(now, timezone.get_current_timezone())
        Logs.objects.create(
            time=now,
            response=mail_status,
            mailing=obj,
            mail=client.email,
            owner=obj.owner
        )
