# Generated by Django 5.0.1 on 2024-01-26 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0011_alter_ventadetalle_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventadetalle',
            name='descuento',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='iva',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='precio_compra',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='precio_venta',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]