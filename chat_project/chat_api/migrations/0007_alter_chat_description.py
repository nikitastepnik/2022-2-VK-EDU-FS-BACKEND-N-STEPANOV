# Generated by Django 4.1.2 on 2022-11-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_api', '0006_rename_chats_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='description',
            field=models.TextField(default='Базовое описание', verbose_name='Описание'),
        ),
    ]