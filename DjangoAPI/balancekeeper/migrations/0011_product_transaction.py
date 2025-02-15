# Generated by Django 3.0.2 on 2020-02-02 16:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('balancekeeper', '0010_auto_20200202_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.DO_NOTHING, to='balancekeeper.Category')),
            ],
            options={
                'db_table': 'product',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('cbk_user_id', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.DO_NOTHING, to='balancekeeper.CbkUser')),
                ('product_id', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.DO_NOTHING, to='balancekeeper.Product')),
            ],
            options={
                'db_table': 'transaction',
                'ordering': ['-date'],
            },
        ),
    ]
