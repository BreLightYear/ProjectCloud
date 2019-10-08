#/usr/bin/env python
# -*- coding:UTF-8 -*-
import uuid
from django.db import models
from .choices import TYPE_SEX, REGION, COUNTRY
from django.utils.translation import gettext_lazy as _
from .validators import validate_CPF, validate_CNPJ

# Create your models here.

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #picture = models.FileField(max_length=100, default='', editable=True)
    active = models.BooleanField( default= False, max_length=20, verbose_name=_('Ativo'))
    name = models.CharField(max_length=50, verbose_name=_('Nome'), help_text=('Nome do Usuário'))
    name2 = models.CharField(max_length=50, verbose_name=_('Sobrenome'), help_text=('Sobrenome do Usuário'))
    email = models.EmailField(max_length=254, verbose_name=_('E-mail'), help_text=('Digite seu e-mail'))
    cpf = models.CharField(unique=True, max_length=12, verbose_name=_('Cpf'), validators=[validate_CPF])
    country = models.CharField(max_length=50, choices=COUNTRY, default=0, verbose_name=_('Pais'))
    region = models.CharField(max_length=50, choices=REGION, default=0, verbose_name=_('Região'))
    adress = models.CharField(max_length=50, verbose_name=_('Endereço'), help_text=('Endereço do Usuário'))
    sex = models.CharField(choices= TYPE_SEX, blank= False, max_length=50, verbose_name=_('Sexo'))
    is_professional = models.BooleanField(max_length=12, default=False, verbose_name=_('Ativo'), help_text=_('Se o usuário for Empresa/Profissional Ativado'))
    #created_in= models.DateTimeField(auto_now_add=False, default=timezone.now)


    def __str__(self):
        return self.name

    def __str__(self):
        return self.id

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=False, max_length=50, verbose_name=_('Ativo'))
    name = models.CharField(max_length=50, blank=True, help_text=('Nome da organização'))
    cnpj = models.CharField(unique=True, validators=[validate_CNPJ], verbose_name=_('CNPJ'), max_length=50)
    adress = models.CharField(max_length=50, verbose_name=_('Endereço')) 
    region = models.CharField(max_length=50, choices=REGION, default=0, verbose_name=_('Região'))

    verbose_name = ['Empresa']
    verbose_name_plural = ['Empresas']
    

    def __str__(self):
        return self.name

class Dots(models.Model):
    person = models.ForeignKey(Person, verbose_name=_("Person"), on_delete=models.CASCADE)
    dots = models.BigIntegerField(editable=False, verbose_name=_('Dots'))