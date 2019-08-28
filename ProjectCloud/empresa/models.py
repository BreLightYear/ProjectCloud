from django.db import models
from choices import COUNTRY, REGION

# Create your models here.


class Empresa(models.Model):
    company= models.CharField(max_length=50, verbose_name=_('Empresa'), help_text=('Digite o nome'))
    country= models.CharField(max_length=50, choices=COUNTRY)
    region= models.CharField(max_length=50, choices=REGION)
    adress= models.CharField(max_length=50, verbose_name=_('Endereço'), help_text=('Digite seu endereço'))


    def __str__(self):
        return self.company
