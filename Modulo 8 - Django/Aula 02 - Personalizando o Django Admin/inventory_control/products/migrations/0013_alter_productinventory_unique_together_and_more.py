# Generated by Django 5.0.1 on 2024-01-30 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_productinventory_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productinventory',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='productinventory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterUniqueTogether(
            name='productinventory',
            unique_together={('product', 'local')},
        ),
    ]
