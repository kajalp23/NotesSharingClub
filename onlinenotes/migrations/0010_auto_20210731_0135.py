# Generated by Django 3.1.7 on 2021-07-30 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinenotes', '0009_auto_20210731_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 31, 1, 35, 57, 951618)),
        ),
    ]