# Generated by Django 4.1.2 on 2023-07-03 07:10

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodShopWebsite', '0003_rename_slug_homemodel_home_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('Home_slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
            ],
        ),
    ]
