from django.db import models


# possivelmente instalar django-phone-field para validação de telefone

class Turma(models.Model):
    turma = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.turma}"


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=24, default='')
    data_nascimento = models.DateField(null=True)

    def __str__(self):
        return f"{self.nome} {self.turma}"


class Responsavel(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.IntegerField(null=True)
    email = models.EmailField(max_length=254, null=True)
    dependente = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} {self.telefone} {self.dependente}"

    class Meta:
        verbose_name = "Responsável"
        verbose_name_plural = "Responsáveis"


class Club(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}"

# -------- Login/Cadastro --------

class Usuario(models.Model):
    matricula = models.CharField(max_length=24)
    data_nascimento = models.DateField(null=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=14, null=True)
    senha = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.matricula}, {self.email}"

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"