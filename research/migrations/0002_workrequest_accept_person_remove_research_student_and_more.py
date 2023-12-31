# Generated by Django 4.0.4 on 2023-10-02 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_clientsystem_is_assistant'),
        ('inventory', '0004_equipment'),
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workrequest',
            name='accept_person',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accept_persons', to='clients.clientsystem', verbose_name='Согласующий'),
        ),
        migrations.RemoveField(
            model_name='research',
            name='student',
        ),
        migrations.AddField(
            model_name='research',
            name='student',
            field=models.ManyToManyField(related_name='student_research', to='clients.clientsystem', verbose_name='Студент'),
        ),
        migrations.RemoveField(
            model_name='research',
            name='teacher',
        ),
        migrations.AddField(
            model_name='research',
            name='teacher',
            field=models.ManyToManyField(related_name='teacher_research', to='clients.clientsystem', verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='work',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work', to='inventory.work', verbose_name='Эксперимент'),
        ),
    ]
