# Generated by Django 5.0.1 on 2024-01-26 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0014_venta_iva_venta_subtotal_alter_venta_cantidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='descuento',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
