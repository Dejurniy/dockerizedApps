# Generated by Django 5.0 on 2023-12-12 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('mark', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]