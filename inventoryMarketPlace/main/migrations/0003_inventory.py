# Generated by Django 5.0.4 on 2024-04-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_customuser_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost_per_item', models.DecimalField(decimal_places=2, max_digits=19)),
                ('quantity_in_stock', models.IntegerField()),
                ('quantity_sold', models.IntegerField(blank=True, null=True)),
                ('sales', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('stock_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]