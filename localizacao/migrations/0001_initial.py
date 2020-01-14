# Generated by Django 3.0.1 on 2020-01-10 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha1', models.CharField(max_length=150)),
                ('linha2', models.CharField(blank=True, max_length=150, null=True)),
                ('cidade', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=70)),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
