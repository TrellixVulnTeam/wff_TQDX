# Generated by Django 2.0.2 on 2018-03-31 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Help_SubCategory_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='HelpSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Help_SubCategory_Name', models.CharField(max_length=100)),
                ('Help_SubCategory_Topic_Id', models.CharField(max_length=100)),
                ('Help_SubCategory_Modified_Date', models.DateField(auto_now_add=True)),
                ('Help_SubCategory_Created_Date', models.DateField(auto_now_add=True)),
                ('Help_SubCategory_Creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='helpsubcategorys', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Help_SubCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help_subcategory.HelpSubCategory'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Help_SubCategory_Comment_Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commenthelpsubcategorys', to=settings.AUTH_USER_MODEL),
        ),
    ]
