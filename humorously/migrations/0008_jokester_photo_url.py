# Generated by Django 2.2.5 on 2019-12-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humorously', '0007_auto_20191208_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='jokester',
            name='photo_url',
            field=models.CharField(default='https://lh4.googleusercontent.com/-QpKk-0G82AE/AAAAAAAAAAI/AAAAAAAAAAg/3r3-YNV9cew/photo.jpg', max_length=255),
        ),
    ]
