# Generated by Django 4.0.1 on 2022-11-20 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_paymentmethod_profile_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_subscribed',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
