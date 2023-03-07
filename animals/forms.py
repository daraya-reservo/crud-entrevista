from django import forms
import requests
from .models import Animal


pacientes = requests.get('https://3y1hl3jca0.execute-api.us-east-1.amazonaws.com/pacientes_endpoint').json()['results']


class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = '__all__'
