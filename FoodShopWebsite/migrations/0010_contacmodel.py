# Generated by Django 4.1.2 on 2023-07-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodShopWebsite', '0009_rename_home_slug_menumodel_menu_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField(default=0)),
                ('address', models.TextField()),
                ('Query', models.TextField()),
            ],
        ),
    ]
