import uuid
from django.db import models
from .choices import COUNTRY, REGION
from django.utils.translation import gettext as _

# Create your models here.


class Empresa(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_('ID EMPRESA'))
    company= models.CharField(max_length=50, verbose_name=_('Empresa'), help_text=('Digite o nome'))
    country= models.IntegerField(choices=COUNTRY, default=0)
    region= models.CharField(max_length=50, choices=REGION, default=0)
    cnpj = models.CharField(unique=True, max_length=14, validators=['validate_CNP'])
    adress= models.CharField(max_length=50, verbose_name=_('Endereço'), help_text=('Digite seu endereço'))


    def __str__(self):
        return self.company
