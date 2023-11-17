# Generated by Django 4.2 on 2023-08-01 16:40

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0013_alter_account_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="avatar",
            field=models.ImageField(
                default="media/avatar.jpg", upload_to=user.models.user_directory_path
            ),
        ),
    ]