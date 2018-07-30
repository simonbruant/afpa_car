# Generated by Django 2.0.5 on 2018-07-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_user_afpa_center'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='music',
            field=models.BooleanField(choices=[(True, 'Oui'), (False, 'Non')], default=False, verbose_name='Musique'),
        ),
        migrations.AddField(
            model_name='user',
            name='smoker',
            field=models.BooleanField(choices=[(True, 'Fumeur'), (False, 'Non Fumeur')], default=False, verbose_name='Fumeur'),
        ),
        migrations.AddField(
            model_name='user',
            name='talker',
            field=models.BooleanField(choices=[(True, 'Tres Bavard'), (False, 'Peu Bavard')], default=False, verbose_name='Bavard'),
        ),
    ]
