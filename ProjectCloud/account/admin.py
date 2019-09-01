from django.contrib import admin
import account, api
from .models import Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    model = Person
    fields= ('name','name2','email','country','region','zip_code','adress','sex','created_in')
