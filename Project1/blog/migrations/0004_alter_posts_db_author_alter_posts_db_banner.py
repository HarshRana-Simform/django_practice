# Generated by Django 4.2 on 2025-03-17 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0003_posts_db_banner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts_db",
            name="author",
            field=models.ForeignKey(
                max_length=100,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="posts_db",
            name="banner",
            field=models.ImageField(
                blank=True, default="fallback.png", upload_to="banners/"
            ),
        ),
    ]
