from clients.models import ClientSystem
from django.db.models import Model, ForeignKey,ManyToManyField, DateField, BooleanField, CharField, TextField
from django.db.models.deletion import CASCADE


class Research(Model):
    name = CharField(max_length=100, verbose_name='Наименование')
    description = TextField(null=True, blank=True)
    student = ManyToManyField(to=ClientSystem, related_name='student_research', verbose_name='Студент')
    teacher = ManyToManyField(to=ClientSystem, related_name='teacher_research', verbose_name='Преподаватель')
    date = DateField()
    class Meta:
        verbose_name = 'Исследование студента'
        verbose_name_plural = 'Исследование студента'

    def __str__(self):
        return "{} ({}) {}".format(self.research.name, self.student, self.teacher, self.date.strftime('%d.%m.%y'))
