# Generated by Django 3.2.4 on 2022-11-09 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_artist_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='slug',
            field=models.SlugField(),
        ),
    ]
