# Generated by Django 3.2.7 on 2021-10-06 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_num_visits'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='num_visits',
            new_name='visits',
        ),
    ]
