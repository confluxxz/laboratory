from django.db.models import Model, ForeignKey, TextField, CharField, BooleanField
from django.db.models.deletion import CASCADE
from .research import Research
from inventory.models.works import Work
from clients.models.client import ClientSystem

class WorkRequest(Model):
    name = CharField(max_length=100, verbose_name='Запрос студента')
    description = TextField(null=True, blank=True)
    student = ForeignKey(to=ClientSystem, on_delete=CASCADE, related_name='student', verbose_name='Студент')
    accept_person = ForeignKey(to=ClientSystem, on_delete=CASCADE, default=None, blank=True, null=True, related_name='accept_persons', verbose_name='Согласующий')
    research = ForeignKey(to=Research, on_delete=CASCADE, related_name='dishes', verbose_name='Исследование')
    is_approved = BooleanField(default=False, blank=True)
    work = ForeignKey(to=Work, on_delete=CASCADE, related_name='work', verbose_name='Эксперимент', default=None, blank=True, null=True)
    class Meta:
        verbose_name = 'Запрос студента на эксперимент'
        verbose_name_plural = 'Запросы студента на эксперименты'

    def __str__(self):
        return "{} {}{}".format(self.name, self.student, self.is_approved, self.accept_person)
