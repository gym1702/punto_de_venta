# Generated by Django 5.0.1 on 2024-01-25 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_proveedor_que_vende'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='web',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
