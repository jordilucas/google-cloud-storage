from django.db import models

class Atracao(models.Model):
    foto = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return self.nome
