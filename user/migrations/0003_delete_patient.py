# Generated by Django 4.2.11 on 2024-03-29 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_remove_visit_patient'),
        ('user', '0002_patient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
