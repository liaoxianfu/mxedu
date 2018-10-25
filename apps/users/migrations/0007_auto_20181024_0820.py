# Generated by Django 2.0.1 on 2018-10-24 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20181023_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='resources/banner/%Y/%m/%d', verbose_name='轮播图'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='resources/image/%Y/%m/%d'),
        ),
    ]
