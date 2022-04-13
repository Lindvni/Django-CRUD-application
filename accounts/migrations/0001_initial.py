# Generated by Django 3.2.4 on 2021-06-24 01:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contractors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('pay_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bill_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('startdate', models.DateField(default=datetime.datetime.now)),
                ('enddate', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
