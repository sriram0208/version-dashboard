# Generated by Django 3.0.6 on 2020-05-12 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_name', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_version', models.CharField(max_length=6)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='version_dashboard.Component')),
                ('release_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='version_dashboard.ReleaseVersion')),
            ],
        ),
    ]
