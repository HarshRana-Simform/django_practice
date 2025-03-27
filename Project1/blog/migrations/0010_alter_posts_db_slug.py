# Generated by Django 4.2 on 2025-03-27 06:51

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_alter_posts_db_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts_db",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                blank=True, editable=True, null=True, populate_from="title"
            ),
        ),
    ]
