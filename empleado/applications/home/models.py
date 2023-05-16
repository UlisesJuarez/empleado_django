from django.db import models

class Prueba(models.Model):
    titulo=models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    cantidad=models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.titulo+"-"+self.subtitulo
