# Generated by Django 3.2.18 on 2023-06-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='fecha_consulta',
            field=models.DateField(null=True, verbose_name='Fecha de consulta'),
        ),
    ]
