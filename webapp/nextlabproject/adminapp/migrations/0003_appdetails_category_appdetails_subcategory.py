# Generated by Django 5.0 on 2023-12-27 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_appdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='appdetails',
            name='category',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appdetails',
            name='subCategory',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
