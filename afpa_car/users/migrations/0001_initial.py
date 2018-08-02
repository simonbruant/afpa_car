# Generated by Django 2.0.5 on 2018-08-02 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carpooling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email adress')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='pseudo')),
                ('first_name', models.CharField(max_length=30, verbose_name='prénom')),
                ('last_name', models.CharField(max_length=50, verbose_name='nom')),
                ('is_active', models.BooleanField(default=True, verbose_name='Utilisateur actif')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name': 'Utilisateur',
                'verbose_name_plural': 'Utilisateurs',
            },
        ),
        migrations.CreateModel(
            name='PrivateData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('afpa_number', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='private_data', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_license', models.BooleanField(choices=[(True, 'Oui'), (False, 'Non')], default=False, verbose_name='permis')),
                ('trainee', models.BooleanField(choices=[(True, 'Stagiare'), (False, 'Employé')], default=False, verbose_name='statut')),
                ('car_owner', models.BooleanField(choices=[(True, 'Oui'), (False, 'Non')], default=False, verbose_name="propriétaire d'un véhicule")),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('smoker', models.BooleanField(choices=[(True, 'Fumeur'), (False, 'Non Fumeur')], default=False, verbose_name='Fumeur')),
                ('talker', models.BooleanField(choices=[(True, 'Tres Bavard'), (False, 'Peu Bavard')], default=False, verbose_name='Bavard')),
                ('music', models.BooleanField(choices=[(True, 'Oui'), (False, 'Non')], default=False, verbose_name='Musique')),
                ('gender', models.CharField(blank=True, choices=[('Man', 'Homme'), ('Woman', 'Femme'), ('Other gender', 'Autre')], max_length=50, null=True)),
                ('afpa_center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carpooling.AfpaCenter')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
