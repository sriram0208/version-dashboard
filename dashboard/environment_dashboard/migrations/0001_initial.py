# Generated by Django 3.0.6 on 2020-05-12 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Environments',
            fields=[
                ('environment_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('environment_type', models.CharField(blank=True, choices=[('DEV', 'Development'), ('SIT', 'Sit'), ('STAG', 'Staging'), ('PREP', 'Preproduction'), ('PROD', 'Production')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(choices=[('LOGIX', 'Logix'), ('EPM', 'Epm'), ('OCD', 'Ocd'), ('MESSAGING', 'Messaging')], max_length=20)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('health_endpoint', models.CharField(blank=True, max_length=50)),
                ('remarks', models.TextField(blank=True, max_length=100)),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environment_dashboard.Environments')),
            ],
            options={
                'unique_together': {('environment', 'service_name')},
            },
        ),
    ]
