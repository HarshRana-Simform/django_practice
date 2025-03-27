# Generated by Django 4.2 on 2025-03-27 06:50

import autoslug.fields
from django.db import migrations
from django.utils.text import slugify


def generate_slugs(apps, schema_editor):
    # Replace with your app and model name
    Blog = apps.get_model('blog', 'Posts_db')
    for blog in Blog.objects.all():
        blog.slug = slugify(blog.title)
        blog.save()


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_alter_posts_db_slug"),
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
