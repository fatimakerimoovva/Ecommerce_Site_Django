# Generated by Django 5.0.6 on 2024-06-26 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='product title'),
            preserve_default=False,
        ),
    ]
