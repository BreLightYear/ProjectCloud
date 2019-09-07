from django.contrib import admin
import account, empresa
from .models import Empresa

# Register your models here.

class Empresadmin(admin.ModelAdmin):
    model = Empresa
    fields = ('company', 'country', 'cnpj')

admin.site.register(Empresa, Empresadmin)