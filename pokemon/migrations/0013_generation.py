# Generated by Django 3.0.4 on 2020-03-25 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0012_auto_20200325_0317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generation', models.CharField(default=None, max_length=15)),
            ],
        ),
    ]