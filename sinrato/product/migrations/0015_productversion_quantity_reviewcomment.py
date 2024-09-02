# Generated by Django 5.0.6 on 2024-08-20 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_color_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='productversion',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity of the product'),
        ),
        migrations.CreateModel(
            name='ReviewComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('review', models.TextField()),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to='product.product')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
