# Generated by Django 4.0.1 on 2022-02-01 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order_totalamount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='totalamount',
            new_name='total',
        ),
    ]
