# Generated by Django 4.1.3 on 2023-01-04 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0016_alter_pedidos_productos_li_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido_intermedio_li',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.productos_li'),
        ),
    ]