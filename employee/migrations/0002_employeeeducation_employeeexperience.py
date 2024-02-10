# Generated by Django 5.0.1 on 2024-02-07 10:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursepg', models.CharField(max_length=100, null=True)),
                ('schoolsclgpg', models.CharField(max_length=200, null=True)),
                ('yearofpassingpg', models.CharField(max_length=20, null=True)),
                ('percentagepg', models.CharField(max_length=20, null=True)),
                ('courseug', models.CharField(max_length=100, null=True)),
                ('schoolsclgug', models.CharField(max_length=200, null=True)),
                ('yearofpassingug', models.CharField(max_length=20, null=True)),
                ('percentageug', models.CharField(max_length=20, null=True)),
                ('coursessc', models.CharField(max_length=100, null=True)),
                ('schoolsclssc', models.CharField(max_length=200, null=True)),
                ('yearofpassingssc', models.CharField(max_length=20, null=True)),
                ('percentagessc', models.CharField(max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c1name', models.CharField(max_length=100, null=True)),
                ('c1designation', models.CharField(max_length=100, null=True)),
                ('c1salary', models.CharField(max_length=100, null=True)),
                ('c1duration', models.CharField(max_length=100, null=True)),
                ('c2name', models.CharField(max_length=100, null=True)),
                ('c2designation', models.CharField(max_length=100, null=True)),
                ('c2salary', models.CharField(max_length=100, null=True)),
                ('c2duration', models.CharField(max_length=100, null=True)),
                ('c3name', models.CharField(max_length=100, null=True)),
                ('c3designation', models.CharField(max_length=100, null=True)),
                ('c3salary', models.CharField(max_length=100, null=True)),
                ('c3duration', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
