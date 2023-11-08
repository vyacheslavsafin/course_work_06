# Generated by Django 4.2.4 on 2023-11-08 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='Почта')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='дата и время последней попытки')),
                ('response', models.BooleanField(blank=True, null=True, verbose_name='Ответ сервера')),
                ('mail', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
        migrations.CreateModel(
            name='MailDistribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField(blank=True, null=True, verbose_name='Время начала рассылки')),
                ('time_end', models.DateTimeField(blank=True, null=True, verbose_name='Время окончания рассылки')),
                ('time_next', models.DateTimeField(blank=True, null=True, verbose_name='Время следующей рассылки')),
                ('frequency', models.CharField(choices=[('ежедневно', 'раз в день'), ('еженедельно', 'раз в неделю'), ('ежемесячно', 'раз в месяц')], max_length=50, verbose_name='Периодичность рассылки')),
                ('status', models.CharField(default='создана', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Тема письма')),
                ('body', models.TextField(verbose_name='Тело письма')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
    ]