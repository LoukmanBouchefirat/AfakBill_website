# Generated by Django 3.2.7 on 2021-09-28 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_newproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newproduct',
            name='category',
        ),
        migrations.AddField(
            model_name='newproduct',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.product'),
        ),
    ]
