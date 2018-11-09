from django.db import models


class Usuario(models.Model):
	cedula=models.CharField(max_length=10)
	numero_matricula=models.CharField(max_length=25)
	apellidos=models.CharField(max_length=25)
	nombres=models.CharField(max_length=25)
	proveniencia=models.CharField(max_length=50)
	carrera=models.CharField(max_length=50)
	trabaja=models.BooleanField(default=True)



