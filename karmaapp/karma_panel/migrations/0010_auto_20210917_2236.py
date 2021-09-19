# Generated by Django 3.2.5 on 2021-09-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karma_panel', '0009_alter_add_product_productimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.FloatField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_quantity',
            field=models.CharField(default='quantity', max_length=100, null=True),
        ),
    ]