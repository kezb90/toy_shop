# Generated by Django 4.2 on 2024-02-28 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_delete_postimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="blog.post",
            ),
        ),
    ]
