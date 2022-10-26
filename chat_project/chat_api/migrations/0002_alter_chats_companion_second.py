# Generated by Django 4.1.2 on 2022-10-26 15:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chats',
            name='companion_second',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comp_second',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Собеседник 2'),
        ),
    ]