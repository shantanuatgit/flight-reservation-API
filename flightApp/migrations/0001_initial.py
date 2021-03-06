# Generated by Django 2.2.13 on 2022-03-22 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=10)),
                ('operating_airlines', models.CharField(max_length=20)),
                ('departure_city', models.CharField(max_length=20)),
                ('arrival_city', models.CharField(max_length=20)),
                ('date_of_departure', models.DateField()),
                ('estimated_time_of_departure', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Passenger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightApp.Passenger')),
                ('flight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightApp.Flight')),
            ],
        ),
    ]
