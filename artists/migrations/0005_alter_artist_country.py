# Generated by Django 3.2.4 on 2022-11-15 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_auto_20221115_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='country',
            field=models.CharField(choices=[('1', 'Việt Nam'), ('2', 'US-UK'), ('3', 'K-POP'), ('4', 'Hoa Ngữ')], default='1', max_length=50),
        ),
    ]
