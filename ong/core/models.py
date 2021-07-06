from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    razon_social = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    mail = models.EmailField()
    fk_servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)

    def __str__(self):
        return self.rut
