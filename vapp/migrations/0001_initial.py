# Generated by Django 3.2.8 on 2021-11-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('camera1', models.CharField(max_length=5)),
                ('camera2', models.CharField(max_length=5)),
                ('staticmap', models.CharField(max_length=10)),
                ('speed', models.CharField(max_length=10)),
                ('avgspeed', models.CharField(max_length=10)),
                ('temperature', models.CharField(max_length=10)),
                ('energystatus', models.CharField(max_length=10)),
                ('fuellevel', models.CharField(max_length=5)),
            ],
        ),
    ]
