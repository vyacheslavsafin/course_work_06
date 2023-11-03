from django.db import models
from mail_distribution import constants
from users.models import User


class Client(models.Model):
    email = models.EmailField(max_length=100, verbose_name="Почта")
    name = models.CharField(max_length=150, verbose_name="Имя")
    comment = models.TextField(verbose_name="Комментарий", **constants.NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **constants.NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name="Тема письма")
    body = models.TextField(verbose_name="Тело письма")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **constants.NULLABLE)

    def __str__(self):
        return f'{self.title} ({self.body})'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class MailDistribution(models.Model):
    time_start = models.DateTimeField(verbose_name="Время начала рассылки", **constants.NULLABLE)
    time_end = models.DateTimeField(verbose_name="Время окончания рассылки", **constants.NULLABLE)
    time_next = models.DateTimeField(verbose_name="Время следующей рассылки", **constants.NULLABLE)
    frequency = models.CharField(max_length=50,
                                 choices=constants.MAILING_FREQUENCY,
                                 verbose_name="Периодичность рассылки")
    status = models.CharField(max_length=50,
                              default=constants.MAILING_CREATED)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение")
    clients = models.ManyToManyField(Client, verbose_name="клиенты")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **constants.NULLABLE)

    def __str__(self):
        return f'{self.clients}, {self.message}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Logs(models.Model):
    time = models.DateTimeField(verbose_name="дата и время последней попытки")
    response = models.BooleanField(verbose_name="Ответ сервера", **constants.NULLABLE)
    mailing = models.ForeignKey(MailDistribution, on_delete=models.CASCADE, verbose_name='Рассылка')
    mail = models.EmailField(max_length=100, verbose_name="Почта", **constants.NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **constants.NULLABLE)

    def __str__(self):
        return f'{self.time} - {self.response}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
