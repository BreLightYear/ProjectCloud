from django.contrib import admin
import account, api
from .models import Person, Company

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    model = Person
    fields = ('active', 'is_professional', 'picture', 'name', 'name2', 'sex', 'cpf', 'email', 'country', 'region', 'adress')
    list_filter = ('active','region')
class CompanyAdmin(admin.ModelAdmin):
    model = Company
    fields = ('name', 'active','name', 'cnpj', 'adress', 'region')
    list_filter = ('active', 'region')


admin.site.register(Person, PersonAdmin)