# Generated by Django 5.0.1 on 2024-01-25 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Supervisor', 'Supervisor'), ('Cajero', 'Cajero'), ('Almacenista', 'Almacenista')], max_length=20, null=True, verbose_name='Tipo de usuario'),
        ),
    ]
