# Generated by Django 3.0.3 on 2020-02-11 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bios',
            old_name='user',
            new_name='username',
        ),
    ]
