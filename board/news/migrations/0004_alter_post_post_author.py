# Generated by Django 4.0.6 on 2022-07-23 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0012_alter_file_file'),
        ('news', '0003_remove_filepost_author_remove_imagepost_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.user'),
        ),
    ]
