# Generated by Django 4.0.1 on 2022-12-06 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='studio',
        ),
    ]
