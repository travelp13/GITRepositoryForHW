# Generated by Django 5.1.4 on 2025-01-17 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=10, unique=True)),
                ('rate_buy', models.DecimalField(decimal_places=4, max_digits=10)),
                ('rate_sell', models.DecimalField(decimal_places=4, max_digits=10)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
