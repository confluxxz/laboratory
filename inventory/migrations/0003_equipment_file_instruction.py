# Generated by Django 4.0.4 on 2023-12-17 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='file_instruction',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=None),
        ),
    ]
