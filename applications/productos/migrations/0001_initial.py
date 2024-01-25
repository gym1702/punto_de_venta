# Generated by Django 5.0.1 on 2024-01-25 21:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
        ('marcas', '0001_initial'),
        ('proveedores', '0003_alter_proveedor_web'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=7)),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=7)),
                ('no_ventas', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('imagenes', models.ImageField(blank=True, null=True, upload_to='fotos/productos')),
                ('stock', models.IntegerField()),
                ('unidad', models.CharField(choices=[('pza', 'pza'), ('kg', 'kg'), ('l', 'l')], default='pza', max_length=50)),
                ('fecha_vencimiento', models.DateTimeField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marcas.marca')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedor')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]