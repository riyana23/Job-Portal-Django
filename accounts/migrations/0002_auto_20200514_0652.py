# Generated by Django 3.0.5 on 2020-05-14 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('employer', 'employer'), ('employee', 'employee')], max_length=100),
        ),
    ]
