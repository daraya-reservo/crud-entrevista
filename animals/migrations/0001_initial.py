# Generated by Django 4.1.7 on 2023-03-07 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_animal', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=15)),
                ('pais', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('paciente', models.CharField(max_length=100)),
            ],
        ),
    ]
