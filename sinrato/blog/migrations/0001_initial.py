# Generated by Django 5.0.6 on 2024-06-21 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='max 100 character', max_length=100, verbose_name='Title of the author')),
                ('description', models.TextField(help_text='max 100 character', max_length=100, verbose_name='Description of the author')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('about', models.TextField(blank=True, help_text='max 200 character', null=True, verbose_name='About of blog')),
            ],
            options={
                'verbose_name': 'Description',
                'verbose_name_plural': 'Descriptions',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='max 100 character', verbose_name='tag of blog')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='max 100 character', max_length=100, verbose_name='Title of the blog')),
                ('content', models.TextField(verbose_name='Content of the blog')),
                ('blog_type', models.IntegerField(choices=[(0, 'Choose'), (1, 'Tech'), (2, 'Food'), (3, 'Fastion'), (4, 'Travel'), (5, 'Lifestyle')], default=0, verbose_name='Type of the blog')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published?')),
                ('author', models.ForeignKey(help_text='max 100 character', max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='author_of_blog', to='blog.author', verbose_name='Author of the blog')),
                ('about', models.OneToOneField(help_text='max 200 character', max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='description_of_blog', to='blog.description', verbose_name='Description of the blog')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
