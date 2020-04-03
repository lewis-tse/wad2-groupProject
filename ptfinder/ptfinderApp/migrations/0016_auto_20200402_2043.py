# Generated by Django 2.2.3 on 2020-04-02 19:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ptfinderApp', '0015_auto_20200402_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 20, 43, 55, 789206)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='t_username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptfinderApp.Trainer'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptfinderApp.UserProfile'),
        ),
        migrations.AlterField(
            model_name='trainer_comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 20, 43, 55, 789206)),
        ),
    ]