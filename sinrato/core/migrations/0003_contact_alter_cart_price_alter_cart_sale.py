# Generated by Django 5.0.6 on 2024-06-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_cart_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email of user')),
                ('subject', models.CharField(max_length=255, verbose_name='subject')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='sale',
            field=models.IntegerField(),
        ),
    ]
