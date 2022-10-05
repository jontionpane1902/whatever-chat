# Generated by Django 4.1.2 on 2022-10-05 15:59

from django.db import migrations, models
import rooms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.UUIDField(default=rooms.models.generate_channel, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'General'), (1, 'Gaming'), (2, 'Music'), (3, 'Education'), (4, 'Movies')])),
            ],
        ),
    ]