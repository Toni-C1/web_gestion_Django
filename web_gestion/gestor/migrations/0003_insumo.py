# Generated by Django 4.1.3 on 2022-11-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0002_producto_created_producto_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
