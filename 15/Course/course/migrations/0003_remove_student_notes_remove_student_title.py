# Generated by Django 4.0.4 on 2022-08-23 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0002_student_github_student_server"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="notes",
        ),
        migrations.RemoveField(
            model_name="student",
            name="title",
        ),
    ]
