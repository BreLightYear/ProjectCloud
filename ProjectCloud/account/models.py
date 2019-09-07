#/usr/bin/env python
# -*- coding:UTF-8 -*-
import uuid
from django.db import models
from .choices import TYPE_SEX, REGION, COUNTRY
from django.utils.translation import gettext_lazy as _
from .validators import validate_CPF, validate_CNPJ

# Create your models here.

class Person(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, verbose_name=_('Nome'), help_text=('Digite seu nome'))
    name2 = models.CharField(max_length=50, verbose_name=_('Sobrenome'), help_text=('Digite seu sobrenome'))
    email = models.EmailField(max_length=254, verbose_name=_('E-mail'), help_text=('Digite seu e-mail'))
    cpf = models.CharField(unique=True, max_length=12, verbose_name=_('CPF'), validators=[validate_CPF])
    country = models.CharField(max_length=50, choices=COUNTRY, default=0, verbose_name=_('Pais'))
    region = models.CharField(max_length=50, choices=REGION, default=0, verbose_name=_('Região'))
    #zip_code = models.ForeignKey(on_delete=models.SET_NULL, blank=True, null=True,)
    adress = models.CharField(max_length=50, verbose_name=_('Endereço'), help_text=('Digite seu endereço'))
    sex = models.CharField(choices= TYPE_SEX, blank= False, max_length=50, verbose_name=_('Sexo'), help_text=('Selecione seu sexo'))
    #created_in= models.DateTimeField(auto_now_add=False, default=timezone.now)


    def __str__(self):
        return self.name

