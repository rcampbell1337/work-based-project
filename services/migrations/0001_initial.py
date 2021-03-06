# Generated by Django 3.2 on 2021-05-31 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('OPAL', '0001_initial'),
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
            name='ReferralSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_referral', models.CharField(max_length=50)),
                ('referral_date', models.DateField()),
                ('initial_contact_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPAL.patient')),
                ('therapist_referring', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPAL.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='Pathway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_date', models.DateField()),
                ('meet_criteria_therapy', models.BooleanField(default=False)),
                ('front_door', models.BooleanField(default=False)),
                ('RAFT', models.BooleanField(default=False)),
                ('CCMT', models.BooleanField(default=False)),
                ('CCMT_date', models.DateField(blank=True, null=True)),
                ('admission_barthel', models.IntegerField(blank=True, null=True)),
                ('discharge_barthel', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPAL.patient')),
                ('referral_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.referralsource')),
            ],
        ),
        migrations.CreateModel(
            name='Discharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_no_reside', models.DateField()),
                ('discharge_date', models.DateField()),
                ('delay_discharge', models.BooleanField(default=False)),
                ('delay_reason', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('discharge_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.dischargeservice')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPAL.patient')),
            ],
        ),
        migrations.CreateModel(
            name='D2A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D2A_completion_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPAL.patient')),
                ('therapist_completing_D2A', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPAL.therapist')),
            ],
        ),
    ]
