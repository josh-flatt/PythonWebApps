# Generated by Django 4.0.4 on 2022-08-10 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("messenger", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="recipient",
            field=models.ForeignKey(
                default="1",
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages_received",
                to="messenger.person",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="author",
            field=models.ForeignKey(
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages_sent",
                to="messenger.person",
            ),
        ),
    ]
