# Generated by Django 3.0.2 on 2020-02-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balancekeeper', '0015_category_cbkuser_product_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbkuser',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
