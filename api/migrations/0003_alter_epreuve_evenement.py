# Generated by Django 5.2 on 2025-07-21 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_evenenement_epreuve_evenement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epreuve',
            name='evenement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='epreuves', to='api.evenement'),
        ),
    ]
