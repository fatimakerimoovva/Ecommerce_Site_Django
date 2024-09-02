# Generated by Django 5.0.6 on 2024-07-14 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_brand_product_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='product_image')),
                ('title', models.CharField(max_length=255, verbose_name='product title')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_image'),
        ),
        migrations.AddField(
            model_name='product',
            name='detail_image',
            field=models.ManyToManyField(related_name='detailimage', to='product.images'),
        ),
    ]
