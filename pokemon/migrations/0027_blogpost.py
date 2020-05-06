# Generated by Django 2.2.11 on 2020-05-06 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0026_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=5000)),
                ('image', models.CharField(blank=True, max_length=50, null=True)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
