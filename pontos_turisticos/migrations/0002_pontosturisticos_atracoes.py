# Generated by Django 3.0.1 on 2020-01-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('pontos_turisticos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.Atracao'),
        ),
    ]
