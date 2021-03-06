# Generated by Django 3.0.5 on 2020-05-14 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200514_0652'),
        ('postjob', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_at', models.DateTimeField(auto_now=True)),
                ('job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='application', to='postjob.PostJob')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.EmployeeProfile')),
            ],
        ),
    ]
