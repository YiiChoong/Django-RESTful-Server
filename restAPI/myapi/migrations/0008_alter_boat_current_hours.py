# Generated by Django 4.1.4 on 2022-12-21 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_alter_boat_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='current_hours',
            field=models.PositiveSmallIntegerField(help_text='hours'),
        ),
    ]