# Generated by Django 4.2.11 on 2024-03-18 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="address",
            field=models.CharField(default="", max_length=255),
        ),
    ]
