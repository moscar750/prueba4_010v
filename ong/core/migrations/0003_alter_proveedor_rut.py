# Generated by Django 3.2.4 on 2021-06-29 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_proveedor_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='rut',
            field=models.CharField(max_length=9, primary_key=True, serialize=False),
        ),
    ]