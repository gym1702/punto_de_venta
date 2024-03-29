# Generated by Django 5.0.1 on 2024-01-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_ventadetalle_descuento_ventadetalle_subtotal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventadetalle',
            name='descuento',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
