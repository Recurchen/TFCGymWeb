# Generated by Django 4.0.1 on 2022-11-15 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_alter_class_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='categories',
        ),
    ]