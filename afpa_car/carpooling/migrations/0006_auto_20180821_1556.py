# Generated by Django 2.0.5 on 2018-08-21 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0005_auto_20180821_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaulttrip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur'),
        ),
    ]
