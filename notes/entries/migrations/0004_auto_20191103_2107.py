# Generated by Django 2.2.6 on 2019-11-03 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_auto_20191103_2029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='entry',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
