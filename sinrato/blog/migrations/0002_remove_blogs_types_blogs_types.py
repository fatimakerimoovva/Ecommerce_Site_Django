# Generated by Django 5.0.6 on 2024-09-03 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='types',
        ),
        migrations.AddField(
            model_name='blogs',
            name='types',
            field=models.ManyToManyField(to='blog.blogtype'),
        ),
    ]
