# Generated by Django 2.2.6 on 2019-12-08 02:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jokester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=150)),
                ('email_address', models.CharField(max_length=150)),
                ('city_residence', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('zipcode', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=150)),
                ('created', models.DateTimeField(default=datetime.datetime(2019, 12, 7, 21, 28, 2, 654330))),
            ],
        ),
    ]
