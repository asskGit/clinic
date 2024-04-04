# Generated by Django 4.2.11 on 2024-04-02 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_remove_doctor_description_remove_doctor_experience_and_more'),
        ('patient', '0002_alter_patient_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='recording',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='doctor.doctor'),
        ),
    ]
