# Generated by Django 3.2 on 2021-05-25 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_discharge_dischargeservice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discharge',
            old_name='discharge_date_no_reside',
            new_name='discharge_date',
        ),
    ]
