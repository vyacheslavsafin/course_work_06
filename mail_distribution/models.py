from django.db import models

from mail_distribution import constants


class Client(models.Model):
    email = models.EmailField(max_length=100, verbose_name="Почта")
    name = models.CharField(max_length=150, verbose_name="Имя")
    comment = models.TextField(verbose_name="Комментарий", **constants.NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name="Тема письма")
    body = models.TextField(verbose_name="Тело письма")

    def __str__(self):
        return f'{self.title} ({self.body})'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class MailDistribution(models.Model):
    time = models.TimeField(verbose_name="Время начала рассылки")
    frequency = models.CharField(max_length=50,
                                 choices=constants.MAILING_FREQUENCY,
                                 verbose_name="Периодичность рассылки")
    status = models.CharField(max_length=50,
                              choices=constants.MAILING_STATUS,
                              default=constants.MAILING_CREATED)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение")
    clients = models.ManyToManyField(Client, verbose_name="клиенты")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f'{self.clients} - {self.message}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Logs(models.Model):
    time = models.DateTimeField(verbose_name="дата и время последней попытки")
    status = models.CharField(max_length=50, verbose_name="Статус попытки")
    response = models.CharField(default=False, verbose_name="Сообщение ошибки", **constants.NULLABLE)
    mailing = models.ForeignKey(MailDistribution, on_delete=models.CASCADE, verbose_name='Рассылка')

    def __str__(self):
        return self.response

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
