# Generated by Django 3.1.3 on 2020-11-10 11:08

import album.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_auto_20201110_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=album.models.random_filename, validators=[django.core.validators.FileExtensionValidator(['jpeg', 'jpg', 'png'])]),
        ),
    ]
