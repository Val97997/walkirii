# Generated by Django 4.2 on 2023-07-31 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="presentation",
            field=models.TextField(blank=True, verbose_name="Short Presentation"),
        ),
    ]