# Generated by Django 2.1.1 on 2018-09-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newtable', '0002_auto_20180923_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=0),
        ),
    ]