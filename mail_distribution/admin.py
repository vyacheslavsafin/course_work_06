from django.contrib import admin

from mail_distribution.models import Client, Message, MailDistribution, Logs


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ('email', 'name', 'comment')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fields = ('title', 'body')


@admin.register(MailDistribution)
class MailDistributionAdmin(admin.ModelAdmin):
    fields = ('clients', 'time', 'frequency', 'status', 'message')


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    fields = ('time', 'status', 'response', 'mailing')
