# Generated by Django 4.0.4 on 2022-06-29 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subastas_app', '0002_alter_categoria_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subastas_app.categoria', to_field='nombre'),
        ),
    ]
