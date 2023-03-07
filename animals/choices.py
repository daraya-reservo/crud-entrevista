import requests

pacientes = requests.get('https://3y1hl3jca0.execute-api.us-east-1.amazonaws.com/pacientes_endpoint').json()['results']
PACIENTE_CHOICES = (
    (str(i+1), f"{pacientes[i]['nombre']} {pacientes[i]['apellido_paterno']} {pacientes[i]['apellido_materno']}") for i in range(len(pacientes))
)

SEX_CHOICES = (
    ('Femenino', 'Femenino',),
    ('Masculino', 'Masculino',),
    ('NS/NR', 'NS/NR',),
)

