# Generated by Django 5.0.6 on 2024-08-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_rename_old_proce_product_old_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='name',
        ),
        migrations.AddField(
            model_name='color',
            name='image',
            field=models.ImageField(default=1, upload_to='color_image'),
            preserve_default=False,
        ),
    ]
