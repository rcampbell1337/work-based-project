# Generated by Django 3.2 on 2021-05-25 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OPAL', '0001_initial'),
        ('services', '0005_auto_20210525_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='DischargeService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Discharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_no_reside', models.DateField()),
                ('discharge_date_no_reside', models.DateField()),
                ('delay_discharge', models.BooleanField(default=False)),
                ('delay_reason', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('discharge_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.dischargeservice')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPAL.patient')),
            ],
        ),
    ]