# Generated by Django 2.2.11 on 2020-04-03 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0021_auto_20200401_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='special_forms',
            field=models.ManyToManyField(blank=True, related_name='special', to='pokemon.Special'),
        ),
    ]
