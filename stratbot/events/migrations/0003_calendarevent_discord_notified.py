# Generated by Django 5.0 on 2024-01-21 23:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0002_alter_calendarevent_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="calendarevent",
            name="discord_notified",
            field=models.BooleanField(default=False),
        ),
    ]