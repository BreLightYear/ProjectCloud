from django import forms
from account.models import Person

class PersonForms(forms.Form):
    model = Person