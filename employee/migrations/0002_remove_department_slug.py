# Generated by Django 4.1 on 2022-11-02 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='slug',
        ),
    ]