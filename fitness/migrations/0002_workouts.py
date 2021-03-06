# Generated by Django 2.0 on 2020-01-22 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workouts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_name', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=50)),
                ('body_section', models.CharField(max_length=60)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('number_of_sets', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
