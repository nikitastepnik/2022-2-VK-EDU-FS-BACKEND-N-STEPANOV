# Generated by Django 4.1.2 on 2022-10-23 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_api', '0004_alter_chats_companion_second'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_seen_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего посещения ресурса'),
        ),
    ]
