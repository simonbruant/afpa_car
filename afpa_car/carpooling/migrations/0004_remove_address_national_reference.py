# Generated by Django 2.0.5 on 2018-09-05 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0003_auto_20180831_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='national_reference',
        ),
    ]
