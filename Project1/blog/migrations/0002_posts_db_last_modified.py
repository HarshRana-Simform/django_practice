# Generated by Django 5.1.6 on 2025-03-07 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="posts_db",
            name="last_modified",
            field=models.DateField(auto_now=True),
        ),
    ]
