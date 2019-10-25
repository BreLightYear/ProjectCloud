from django import forms
from .models import Person

class PersonForms(forms.Form):
    model = Person
    fields = ('id','is_professional', 'name', 'name2' , 'email', 'cpf', 'country', 'region', 'adress', 'sex')