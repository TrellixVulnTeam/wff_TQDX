# Generated by Django 2.0.2 on 2018-03-24 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Location_Amenitie', '0002_auto_20180324_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location_amenitie',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='location_amenitie',
            name='modified_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
