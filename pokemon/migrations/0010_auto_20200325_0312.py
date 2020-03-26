# Generated by Django 3.0.4 on 2020-03-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0009_auto_20200325_0303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('Kanto', 'Kanto'), ('Johto', 'Johto'), ('Hoenn', 'Hoenn'), ('Sinnoh', 'Sinnoh'), ('Unova', 'Unova'), ('Kalos', 'Kalos'), ('Alola', 'Alola'), ('Galar', 'Galar')], default=None, max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Generation',
        ),
    ]