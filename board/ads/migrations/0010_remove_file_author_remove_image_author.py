# Generated by Django 4.0.6 on 2022-07-22 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0009_remove_ad_ad_images_ad_ad_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='author',
        ),
        migrations.RemoveField(
            model_name='image',
            name='author',
        ),
    ]
