# Generated by Django 3.2 on 2021-05-26 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_rename_discharge_date_no_reside_discharge_discharge_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='d2a',
            old_name='therapist_completing_d2a',
            new_name='therapist_completing_D2A',
        ),
        migrations.AlterField(
            model_name='discharge',
            name='delay_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]