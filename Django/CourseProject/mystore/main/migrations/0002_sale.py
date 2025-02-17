# Generated by Django 5.1.4 on 2025-01-19 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Назва акції')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Опис акції')),
                ('image', models.ImageField(blank=True, null=True, upload_to='sales/', verbose_name='Изображение')),
                ('start_date', models.DateTimeField(verbose_name='Дата початку акції')),
                ('end_date', models.DateTimeField(verbose_name='Дата закінчення акції')),
            ],
            options={
                'verbose_name': 'Акція',
                'verbose_name_plural': 'Акції',
                'db_table': 'sale',
                'ordering': ['name'],
            },
        ),
    ]
