# Generated by Django 2.0.5 on 2018-07-30 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20180730_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatedata',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='private_data', to=settings.AUTH_USER_MODEL),
        ),
    ]