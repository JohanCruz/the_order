# Generated by Django 3.2.14 on 2022-07-30 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_productorder_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='carry_off',
            field=models.BooleanField(default=False),
        ),
    ]