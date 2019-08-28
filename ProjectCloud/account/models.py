from django.db import models
from choices import TYPE_SEX, REGION, COUNTRY
from django.utils.translation import gettext_lazy as _
from geography.models import ZipCode

# Create your models here.

class Person(models.Model):
    name= models.CharField(max_length=50, verbose_name=_('Nome'), help_text=('Digite seu nome'))
    name2= models.CharField(max_length=50, verbose_name=_('Sobrenome'), help_text=('Digite seu sobrenome'))
    email= models.EmailField(max_length=254, verbose_name=_('E-mail'), help_text=('Digite seu e-mail'))
    country= models.CharField(max_length=50, choices=COUNTRY)
    region= models.CharField(max_length=50, choices=REGION)
    zip_code = models.ForeignKey(ZipCode, on_delete=models.SET_NULL, blank=True, null=True,)
    adress= models.CharField(max_length=50, verbose_name=_('Endereço'), help_text=('Digite seu endereço'))
    sex= models.CharField(choices=blank= False, max_length=50, verbose_name=_('Sexo'), help_text=('Selecione seu sexo'))
    created_in= models.DateTimeField(auto_now=False)


    def __str__(self):
        return self.name


class Empresa(models.Model):
    company= models.CharField(max_length=50, verbose_name=_('Empresa'), help_text=('Digite o nome'))
    country= models.CharField(max_length=50, choices=COUNTRY)
    region= models.CharField(max_length=50, choices=REGION)
    adress= models.CharField(max_length=50, verbose_name=_('Endereço'), help_text=('Digite seu endereço'))


    def __str__(self):
        return self.company
