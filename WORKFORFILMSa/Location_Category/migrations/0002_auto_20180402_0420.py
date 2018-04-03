# Generated by Django 2.0.2 on 2018-04-02 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Location_Category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Comment_Location',
            new_name='Comment_Location_Category',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Location_Comment',
            new_name='Location_Category_Comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Location_Comment_Author',
            new_name='Location_Category_Comment_Author',
        ),
        migrations.RenameField(
            model_name='location_category',
            old_name='created_date',
            new_name='Location_Category_Created_Date',
        ),
        migrations.RenameField(
            model_name='location_category',
            old_name='Creator',
            new_name='Location_Category_Creator',
        ),
        migrations.RenameField(
            model_name='location_category',
            old_name='modified_Date',
            new_name='Location_Category_Modified_Date',
        ),
        migrations.RenameField(
            model_name='location_category',
            old_name='Category_No',
            new_name='Location_Category_Name',
        ),
        migrations.RenameField(
            model_name='location_category',
            old_name='Location_Categoryname',
            new_name='Location_Category_No',
        ),
    ]
