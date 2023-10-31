from mail_distribution.utils import mail_worker


def my_scheduled_job():
    mail_worker()