# Generated by Django 3.0.2 on 2020-02-09 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balancekeeper', '0017_auto_20200209_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbkuser',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
