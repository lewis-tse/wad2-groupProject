# Generated by Django 2.2.3 on 2020-04-02 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptfinderApp', '0014_auto_20200402_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 20, 35, 13, 921895)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='t_username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trainer_comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 20, 35, 13, 921895)),
        ),
    ]
