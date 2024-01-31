# Generated by Django 5.0.1 on 2024-01-27 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_descuento'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descuento',
            field=models.FloatField(blank=True, null=True, verbose_name='Porcentaje de descuento'),
        ),
        migrations.AddField(
            model_name='producto',
            name='fecha_fin_descuento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de fin de descuento'),
        ),
        migrations.AddField(
            model_name='producto',
            name='fecha_inicio_descuento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de inicio de descuento'),
        ),
        migrations.DeleteModel(
            name='Descuento',
        ),
    ]
