# Generated by Django 4.0.6 on 2022-07-22 20:43

import ads.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0011_remove_ad_ad_files_ad_ad_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(null=True, upload_to=ads.models.ad_author_directory_path, validators=[django.core.validators.FileExtensionValidator(['mp4'])]),
        ),
    ]
