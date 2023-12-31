# Generated by Django 4.0.4 on 2023-10-02 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_clientsystem_is_assistant'),
        ('inventory', '0003_workdishes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название оборудования')),
                ('is_avaliabe', models.BooleanField(default=True, verbose_name='Готов к работе')),
                ('place', models.CharField(default='', max_length=500, verbose_name='Место хранения')),
                ('experiment_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment', to='inventory.work', verbose_name='Работа')),
                ('laboratory_assistant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laboratory_assistant', to='clients.clientsystem', verbose_name='Ответственный за оборудование')),
            ],
            options={
                'verbose_name': 'Оборудование эксперимента',
                'verbose_name_plural': 'Оборудование эксперимента',
            },
        ),
    ]
