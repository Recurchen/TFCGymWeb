# Generated by Django 4.0.1 on 2022-11-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0014_alter_classinstance_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='all_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
