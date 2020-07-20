# Generated by Django 2.2 on 2020-07-20 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20200719_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='created_by',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='updated_by',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='created_by',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='updated_by',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='created_by',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='updated_by',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='created_by',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='updated_by',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='created_by',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='updated_by',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
    ]
