# Generated by Django 3.0.1 on 2020-01-10 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('pontos_turisticos', '0003_pontosturisticos_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.Avaliacao'),
        ),
    ]
