# Generated by Django 5.2 on 2025-07-02 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='epreuve',
            old_name='evenenement',
            new_name='evenement',
        ),
    ]
