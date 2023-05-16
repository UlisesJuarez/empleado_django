from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name="Habilidad"
        verbose_name_plural="Habilidades Empleados"
    
    def __str__(self):
        return str(self.id)+"-"+self.habilidad


class Empleado(models.Model):
    """Modelo para tabla empleado"""

    jobs=(('0','Contador'),
          ('1','Programador'),
          ('2','Economista'),
          ('3','Otro'),)

    first_name = models.CharField("Nombres", max_length=60)
    last_name = models.CharField("Apellidos", max_length=60)
    job = models.CharField("Job", max_length=1,choices=jobs)
    full_name=models.CharField("Nombre completo",
                               max_length=120,
                               blank=True)
    #relacion de uno a muchos
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='empleado',blank=True,null=True)

    #relacion de muchos a muchos
    habilidades = models.ManyToManyField(Habilidades)

    #para usar el ckeditor
    hoja_vida= RichTextField()



    class Meta:
        verbose_name="Mi empleado"
        verbose_name_plural="Empleados de la empresa"
        ordering=['-first_name','last_name']
        unique_together=("first_name","departamento")

    def __str__(self):
        return str(self.id)+"-"+self.first_name+"-"+self.last_name