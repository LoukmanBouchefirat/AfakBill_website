# Generated by Django 3.2.7 on 2021-10-06 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_num_visits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='num_visits',
            field=models.TextField(default=None, null=True),
        ),
    ]