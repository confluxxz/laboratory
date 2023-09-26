from django.db.models import Model, CharField, TextField, IntegerField, DateTimeField


class Dishes(Model):
    name = CharField(max_length=100, verbose_name='Наименование')
    quantity = IntegerField(default=0, verbose_name='Количество')
    place = CharField(max_length=500, default="", verbose_name="Место хранения")
    last_update_date = DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')


    class Meta:
        verbose_name = 'Посуда'
        verbose_name_plural ='Лабораторная посуда'

    def __str__(self):
        return self.name
