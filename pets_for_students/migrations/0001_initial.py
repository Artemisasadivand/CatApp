# Generated by Django 5.0.3 on 2024-03-21 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, unique=True)),
                ('last_name', models.CharField(max_length=128, unique=True)),
                ('number_of_cats', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets_for_students.student')),
            ],
            options={
                'verbose_name_plural': 'Cats',
            },
        ),
    ]
