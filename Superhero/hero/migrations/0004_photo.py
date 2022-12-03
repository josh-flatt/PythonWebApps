# Generated by Django 4.1.1 on 2022-12-03 00:46

from django.db import migrations, models
import hero.models


class Migration(migrations.Migration):

    dependencies = [
        ("hero", "0003_rename_author_investigator_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
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
                ("title", models.CharField(max_length=100)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to=hero.models.get_upload
                    ),
                ),
            ],
        ),
    ]
