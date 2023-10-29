NULLABLE = {'blank': True, 'null': True}

DAILY = 'ежедневно'
WEEKLY = 'еженедельно'
MONTHLY = 'ежемесячно'

MAILING_FREQUENCY = [
    (DAILY, 'раз в день'),
    (WEEKLY, 'раз в неделю'),
    (MONTHLY, 'раз в месяц'),
]

MAILING_CREATED = 'создана'
MAILING_ACTIVE = 'запущена'
MAILING_FINISHED = 'приостановлена'
MAILING_STATUS = [
    (MAILING_CREATED, 'Создана'),
    (MAILING_ACTIVE, 'Запущена'),
    (MAILING_FINISHED, 'Приостановлена'),
]