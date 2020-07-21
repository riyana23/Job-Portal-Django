# Generated by Django 3.0.5 on 2020-05-16 06:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postjob', '0004_auto_20200515_1751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobapplication',
            options={'ordering': ['rank']},
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='rank',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='applied_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]