# Generated by Django 5.0.4 on 2024-04-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_inventory_sale_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
