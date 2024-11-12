from django.db import models

class Volunteers(models.Model):
    profissao = models.CharField(max_length=30, blank=False, null=False)
    empresa = models.CharField(max_length=30, blank=False, null=False)
    cargo = models.CharField(max_length=30, blank=False, null=False)
    habilitação = models.CharField(max_length=30, blank=False, null=False)
    dirige = models.CharField(max_length=30, blank=False, null=False)
    possui_carro = models.CharField(max_length=30, blank=False, null=False)
    cargo_voluntario = models.CharField(max_length=30, blank=False, null=False)
    nome = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False)
    nasc = models.CharField(max_length=30, blank=False, null=False)
    whats = models.CharField(max_length=30, blank=False, null=False)
    cep = models.CharField(max_length=30, blank=False, null=False)
    bairro = models.CharField(max_length=30, blank=False, null=False)
    endereco = models.CharField(max_length=30, blank=False, null=False)

class Adopt(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False)
    nasc = models.CharField(max_length=30, blank=False, null=False)
    cep = models.CharField(max_length=30, blank=False, null=False)
    bairro = models.CharField(max_length=30, blank=False, null=False)
    endereco = models.CharField(max_length=30, blank=False, null=False)
    profissao = models.CharField(max_length=30, blank=False, null=False)
    dog_name = models.CharField(max_length=30, blank=False, null=False)

class sponsor(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False)
    cpf = models.CharField(max_length=30, blank=False, null=False)
    cep = models.CharField(max_length=30, blank=False, null=False)
    bairro = models.CharField(max_length=30, blank=False, null=False)
    endereco = models.CharField(max_length=30, blank=False, null=False)
    dog_name = models.CharField(max_length=30, blank=False, null=False)
    valor_mensal = models.CharField(max_length=30, blank=False, null=False)
    recebimento = models.CharField(max_length=30, blank=False, null=False)