# Generated by Django 4.0.4 on 2023-12-17 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_equipment_file_instruction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='is_approved',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Одобрено'),
        ),
    ]
