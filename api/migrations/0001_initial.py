# Generated by Django 5.2 on 2025-07-02 18:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('horraire', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Epreuve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epreuves', to='api.discipline')),
                ('evenenement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epreuves', to='api.evenement')),
            ],
        ),
        migrations.AddField(
            model_name='evenement',
            name='lieu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evenements', to='api.lieu'),
        ),
    ]
