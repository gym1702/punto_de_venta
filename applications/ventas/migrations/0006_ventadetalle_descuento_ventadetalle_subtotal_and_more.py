# Generated by Django 5.0.1 on 2024-01-26 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_remove_ventadetalle_descuento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventadetalle',
            name='descuento',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='ventadetalle',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='ventadetalle',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
