from django.db import models
from django.contrib.auth.models import AbstractUser


'''é o usuario'''
class Usuario(AbstractUser):
    TIPO_CHOICES = [
        ('G','Gestor'),
        ('P','Professor'),
    ]

    tipo = models.CharField(max_length=200, choices=TIPO_CHOICES, default='P') #esse é um campo opcional de escolha, se não escolher vai o padrao "P"
    ni = models.IntegerField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True) #esse é um campo opcional, é aceito o null (nada)
    data_nascimento = models.DateField()
    data_contratacao = models.DateField()

    REQUIRED_FIELDS=['ni', 'data_nascimento','data_contratacao', 'tipo'] #sao os campos obrigatorios de preenchimento
    def __str__(self):
        return f'{self.username}, {self.get_tipo_display()}' #get_nomedoCHOICE_display serve para mostrar o display ou seja, inves de P mostra PROFESSOR

class Disciplina (models.Model):
    nome = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)
    professor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'tipo': 'P'})

    def __str__(self):
        return self.nome
    
class Sala(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    def __str__(self):
        return self.nome
    
class ReservaAmbiente(models.Model):

    PERIODO_CHOICES = [
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('Noite', 'Noite')
    ]

    data_inicio = models.DateField()
    data_termino = models.DateField()
    periodo = models.CharField(max_length=255, choices=PERIODO_CHOICES, default='M')
    sala_reservada = models.ForeignKey(Sala, on_delete=models.CASCADE) #CASCADE pois se uma sala não existe, logo a reserva não pode existir
    professsor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo': 'P'})
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sala_reservada} - No período: {self.get_periodo_display()}, Horário: {self.data_inicio} até {self.data_termino}'