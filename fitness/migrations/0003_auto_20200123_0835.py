# Generated by Django 2.0 on 2020-01-23 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0002_workouts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='media/'),
        ),
    ]
