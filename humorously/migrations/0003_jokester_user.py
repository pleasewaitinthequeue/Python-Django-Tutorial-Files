# Generated by Django 2.2.6 on 2019-12-08 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('humorously', '0002_auto_20191208_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='jokester',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
