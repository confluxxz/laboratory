# Generated by Django 4.0.4 on 2023-09-26 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
    ]
