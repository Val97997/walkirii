# Generated by Django 4.2 on 2023-08-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_alter_account_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="avatar",
            field=models.ImageField(default="avatars/avatar.jpg", upload_to="avatars/"),
        ),
    ]
