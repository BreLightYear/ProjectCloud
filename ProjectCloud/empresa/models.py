from django.db import models
from .choices import COUNTRY, REGION
from account.validators import validate_CNPJ
from django.utils.translation import gettext as _

# Create your models here.


class Empresa(models.Model):
    company= models.CharField(max_length=50, verbose_name=_('Empresa'), help_text=('Digite o nome'))
    country= models.IntegerField(choices=COUNTRY, default=0)
    region= models.CharField(max_length=50, choices=REGION, default=0)
    cnpj = models.CharField(unique=True, max_length=14, validators=[validate_CNPJ])
    adress= models.CharField(max_length=50, verbose_name=_('Endereço'), help_text=('Digite seu endereço'))


    def __str__(self):
        return self.company
