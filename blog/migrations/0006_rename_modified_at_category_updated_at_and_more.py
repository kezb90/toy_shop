# Generated by Django 4.2 on 2024-02-19 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_category_description_alter_post_body"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="modified_at",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="modified_at",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="image",
            old_name="modified_at",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="modified_at",
            new_name="updated_at",
        ),
    ]