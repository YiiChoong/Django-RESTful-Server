# Generated by Django 4.1.4 on 2022-12-20 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_car_delete_cars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='vin',
            field=models.CharField(max_length=17),
        ),
    ]
