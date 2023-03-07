from django import forms
from .models import Animal


class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = '__all__'

    def clean_id_animal(self):
        id_animal = self.cleaned_data['id_animal'].upper().replace("-", "").replace(".", "")
        rut = id_animal[:-1]
        dv = id_animal[-1:]
        if not rut.isnumeric() or not(dv.isnumeric() or dv == 'K'):
            raise forms.ValidationError('El ID debe tener el formato de RUT chileno')
        return f"{rut}-{dv}"
