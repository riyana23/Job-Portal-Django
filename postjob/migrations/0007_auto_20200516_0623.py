# Generated by Django 3.0.5 on 2020-05-16 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postjob', '0006_auto_20200516_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='rank',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
