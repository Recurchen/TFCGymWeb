# Generated by Django 4.0.1 on 2022-12-07 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_classinstance_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classinstance',
            name='categories',
        ),
    ]
