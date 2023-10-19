from django.db import models
from django.contrib.auth.models import User

class Room_Class(models.Model):
    room_class = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.room_class}"
    
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


class TimeTable(models.Model):
    room_class = models.ForeignKey(Room_Class, on_delete=models.CASCADE)

    in_time = models.DateTimeField(max_length=60)
    out_time = models.DateTimeField(max_length=60)


class Club(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


USER_TYPE_CHOICES = [
    ('aluno', 'Aluno(a)'),
    ('professor', 'Professor(a)'),
    ('responsavel', 'Responsável'),
    ('diretoria', 'Diretoria'),
]


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, to_field="username")
    room_class = models.ForeignKey(Room_Class, on_delete=models.CASCADE, null=True, blank=True)
    dependent = models.ManyToManyField(User, related_name='user_dependent', blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True)

    student_id = models.CharField(max_length=24, null=True, blank=True)
    type = models.CharField(max_length=40, choices=USER_TYPE_CHOICES)
    birthdate = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return f"{self.student_id}, {self.user.username}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
