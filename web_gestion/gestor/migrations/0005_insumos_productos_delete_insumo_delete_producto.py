# Generated by Django 4.1.3 on 2022-12-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0004_alter_insumo_options_alter_producto_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insumos',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Últa modificación')),
            ],
            options={
                'verbose_name': 'Insumo',
                'verbose_name_plural': 'Insumos',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.DeleteModel(
            name='Insumo',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]