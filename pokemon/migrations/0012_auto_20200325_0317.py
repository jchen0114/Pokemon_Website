# Generated by Django 3.0.4 on 2020-03-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0011_pokemon_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='region',
            field=models.CharField(default=None, max_length=10),
        ),
    ]