from django.contrib import admin
import account, api
from .models import Person, Empresa

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    fields= ('name','name2','email','country','region','zip_code','adress','sex','created_in')

class AdminEmpresa(admin.ModelAdmin):
    admin.site.register(Empresa)