# Generated by Django 4.0.4 on 2022-06-27 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subastas_app', '0003_alter_subasta_precio_ganador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subasta',
            name='precio_ganador',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
