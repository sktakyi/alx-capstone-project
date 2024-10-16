# Generated by Django 5.1.2 on 2024-10-16 18:09

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('contact_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('contact_address', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='inventory.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=20, unique=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Completed'), ('R', 'Refunded'), ('S', 'Shipped')], default='P', max_length=1)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.customer')),
                ('products', models.ManyToManyField(to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_quantity', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
    ]
