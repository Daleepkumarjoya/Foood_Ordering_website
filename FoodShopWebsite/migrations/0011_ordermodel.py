# Generated by Django 4.1.2 on 2023-07-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodShopWebsite', '0010_contacmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField(default=0)),
                ('foodName', models.CharField(max_length=200)),
                ('AdditionalFood', models.CharField(max_length=200)),
                ('myDate', models.DateTimeField(auto_now=True)),
                ('address', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
