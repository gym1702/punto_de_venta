# Generated by Django 5.0.1 on 2024-01-25 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=100, verbose_name='Razon social')),
                ('rfc', models.CharField(blank=True, max_length=20, null=True, verbose_name='RFC')),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('web', models.EmailField(blank=True, max_length=100, null=True)),
                ('calle_no', models.CharField(blank=True, max_length=200, null=True)),
                ('colonia', models.CharField(blank=True, max_length=200, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.CharField(blank=True, max_length=200, null=True)),
                ('cp', models.CharField(blank=True, max_length=10, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('credito', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='No', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
