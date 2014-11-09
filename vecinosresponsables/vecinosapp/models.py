from django.db import models
# Create your models here.


class Aviso(models.Model):
    comentario = models.TextField(blank=False)
    imagen = models.ImageField(null=True, blank=True,
        upload_to='',)
    mail = models.EmailField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    latitud = models.FloatField()
    longitud = models.FloatField()
    resuelto = models.BooleanField(default=False)

    def __unicode__(self):
        return self.id