# Generated by Django 5.0.1 on 2024-01-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_remove_empresa_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='logo_principal',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='logo_secundario',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre_corto',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre'),
        ),
    ]