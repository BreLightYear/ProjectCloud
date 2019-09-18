from django.contrib import admin
import account, api
from .models import Person, Company

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    model = Person
    fields = ('active', 'name', 'name2', 'sex', 'cpf', 'email', 'country', 'region', 'adress')
    list_filter = ('active','region')
class CompanyAdmin(admin.ModelAdmin):
    model = Company
    fields = ('name', 'active', 'cnpj', 'adress', 'region')


admin.site.register(Person, PersonAdmin)