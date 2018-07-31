# Generated by Django 2.0.6 on 2018-07-31 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_label_public', models.CharField(blank=True, max_length=50, null=True, verbose_name="Libellé de l'adresse public")),
                ('street_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Numéro de la rue')),
                ('street_name', models.CharField(max_length=100, verbose_name='Nom de la rue')),
                ('street_complement', models.CharField(blank=True, max_length=100, null=True, verbose_name="Complément d'adresse")),
                ('lattitude', models.DecimalField(blank=True, decimal_places=25, max_digits=25, null=True, verbose_name='lattitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=25, max_digits=25, null=True, verbose_name='longitude')),
            ],
            options={
                'verbose_name': 'Adresse',
            },
        ),
        migrations.CreateModel(
            name='Address_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_label_private', models.CharField(blank=True, default='Adresse', max_length=100, null=True, verbose_name='Libellé privé')),
            ],
        ),
        migrations.CreateModel(
            name='AfpaCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_name', models.CharField(max_length=50, verbose_name='Nom du centre')),
            ],
            options={
                'verbose_name': 'Centre AFPA',
                'verbose_name_plural': 'Centres AFPA',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50, verbose_name='Couleur')),
                ('model', models.CharField(max_length=50, verbose_name='Modèle')),
                ('consumption', models.FloatField(verbose_name='Consommation (en l/100km)')),
                ('fuel', models.CharField(choices=[('SP-98', 'SP-98'), ('SP-95', 'SP-95'), ('SP-95 E10', 'SP-95 E10'), ('DIESEL', 'DIESEL'), ('GPL', 'GPL'), ('ELECTRIQUE', 'ELECTRIQUE')], max_length=20, verbose_name='Type de carburant')),
                ('amount_of_free_seats', models.IntegerField(default=1, verbose_name='Nombre de places libres')),
            ],
            options={
                'verbose_name': 'Voiture',
                'verbose_name_plural': 'Voitures',
            },
        ),
        migrations.CreateModel(
            name='Car_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carpooling.Car', verbose_name='Vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=60, verbose_name='Ville')),
            ],
            options={
                'verbose_name': 'Ville',
                'verbose_name_plural': 'Villes',
            },
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formation_name', models.CharField(max_length=50, verbose_name='Libellé de la Formation')),
            ],
            options={
                'verbose_name': 'Formation',
                'verbose_name_plural': 'Formations',
            },
        ),
        migrations.CreateModel(
            name='FormationSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formation_session_start_date', models.DateField(verbose_name='Date de début de formation')),
                ('formation_session_end_date', models.DateField(verbose_name='Date de fin de formation')),
                ('work_experience_start_date', models.DateField(verbose_name='Date de début de stage')),
                ('work_experience_end_date', models.DateField(verbose_name='Date de fin de stage')),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carpooling.Formation', verbose_name='Formation')),
            ],
            options={
                'verbose_name': 'Session de formation',
                'verbose_name_plural': 'Sessions de formations',
            },
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=15, verbose_name='Code Postal')),
            ],
            options={
                'verbose_name': 'Code Postal',
                'verbose_name_plural': 'Codes Postaux',
            },
        ),
        migrations.CreateModel(
            name='ZipCode_City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carpooling.City', verbose_name='Villes')),
                ('zip_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carpooling.ZipCode', verbose_name='Code Postal')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='zip_codes',
            field=models.ManyToManyField(through='carpooling.ZipCode_City', to='carpooling.ZipCode', verbose_name='Code Postal'),
        ),
    ]
