# Generated by Django 3.1.4 on 2021-09-16 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinenotes', '0015_notification_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('msg', models.CharField(max_length=300)),
            ],
        ),
    ]
