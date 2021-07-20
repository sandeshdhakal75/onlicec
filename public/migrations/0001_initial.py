# Generated by Django 3.1.3 on 2021-01-12 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Public',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('crime_location', models.CharField(max_length=100)),
                ('complain_description', models.CharField(max_length=30)),
                ('date_of_crime', models.DateField(blank=True, null=True)),
                ('time_of_crime', models.TimeField(blank=True, null=True)),
                ('evidence', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('contact_number', models.CharField(max_length=14)),
                ('complaint_type', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Others')], max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]