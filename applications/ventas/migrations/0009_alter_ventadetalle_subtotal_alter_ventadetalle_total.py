# Generated by Django 5.0.1 on 2024-01-26 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0008_alter_ventadetalle_producto_alter_ventadetalle_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventadetalle',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=20, null=True),
        ),
    ]
