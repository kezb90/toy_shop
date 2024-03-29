# Generated by Django 4.2 on 2024-02-19 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_rename_modified_at_category_updated_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="Is active"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date created"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="date updated"),
                ),
                ("image", models.ImageField(upload_to="Blog_images/")),
                ("alt", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.post"
                    ),
                ),
            ],
            options={
                "ordering": ("pk",),
                "abstract": False,
            },
        ),
    ]
