# Generated by Django 2.0.2 on 2018-03-24 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='Budget',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='Location_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='Location_latitude',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='Location_longitude',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='Pincode',
            field=models.IntegerField(),
        ),
    ]
