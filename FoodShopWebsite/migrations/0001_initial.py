# Generated by Django 4.1.2 on 2023-07-02 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Desc', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
