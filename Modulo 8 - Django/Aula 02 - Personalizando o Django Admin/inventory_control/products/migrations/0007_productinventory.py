# Generated by Django 5.0.1 on 2024-01-30 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_suppliers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=8)),
                ('local', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', unique=True)),
            ],
            options={
                'verbose_name': 'Quantidade do Produto',
                'verbose_name_plural': 'Quantidades dos Produtos',
                'unique_together': {('product', 'local')},
            },
        ),
    ]