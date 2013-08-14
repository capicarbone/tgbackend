from django.db import models


class Doctor(models.Model):
	nombre = models.CharField(max_length=50)
	especialidades = models.CharField(max_length=120)
	correo = models.EmailField(max_length=80)
	validado = models.BooleanField(default=False)
	fecha_registro = models.DateTimeField(auto_now_add=True)

