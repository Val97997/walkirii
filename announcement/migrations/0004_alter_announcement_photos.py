# Generated by Django 4.2 on 2023-08-03 19:20

import announcement.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("announcement", "0003_announcement_photos"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="photos",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=announcement.models.announcement_photos_directory_path,
            ),
        ),
    ]
