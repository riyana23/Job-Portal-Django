# Generated by Django 3.0.8 on 2020-07-18 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postjob', '0007_auto_20200516_0623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobapplication',
            options={'ordering': ['-rank']},
        ),
    ]
