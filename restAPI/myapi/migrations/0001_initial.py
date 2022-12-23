# Generated by Django 4.1.4 on 2022-12-20 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=60)),
                ('model', models.CharField(max_length=60)),
                ('year', models.PositiveSmallIntegerField()),
                ('seats', models.PositiveSmallIntegerField()),
                ('color', models.CharField(max_length=60)),
                ('vin', models.PositiveIntegerField()),
                ('curr_mileage', models.PositiveIntegerField(verbose_name='miles')),
                ('service_interval', models.PositiveIntegerField(verbose_name='miles')),
                ('next_service', models.PositiveIntegerField(verbose_name='miles')),
            ],
        ),
    ]