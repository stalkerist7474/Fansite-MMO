# Generated by Django 4.0.6 on 2022-07-26 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0004_remove_myuser_birhtday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
