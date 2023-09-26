# Generated by Django 4.0.4 on 2023-09-26 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_alter_dishes_quantity'),
        ('inventory', '0002_work_alter_reagents_place_alter_reagents_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkDishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество')),
                ('dishes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.dishes', verbose_name='Посуда')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='inventory.work', verbose_name='Работа')),
            ],
            options={
                'verbose_name': 'Посуда эксперимента',
                'verbose_name_plural': 'Посуда эксперимента',
            },
        ),
    ]
