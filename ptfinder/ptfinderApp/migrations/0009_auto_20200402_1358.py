# Generated by Django 3.0.4 on 2020-04-02 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptfinderApp', '0008_auto_20200401_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 13, 58, 36, 609501)),
        ),
        migrations.AlterField(
            model_name='trainer_comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 13, 58, 36, 609501)),
        ),
    ]
