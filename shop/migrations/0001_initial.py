# Generated by Django 3.2.9 on 2022-11-15 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=201)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('category', models.CharField(max_length=201)),
                ('description', models.TextField(max_length=799)),
                ('image', models.CharField(max_length=301)),
            ],
        ),
    ]
