from django.contrib import admin
import account, api
from .models import Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    model = Person
    fields= ('name', 'name2', 'email', 'country', 'region', 'adress', 'sex', 'user_photo')

admin.site.register(Person, PersonAdmin)