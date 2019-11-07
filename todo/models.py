from django.db import models

class Post(models.Model):
    texto = models.TextField()

    def __str__(self):
        return str(self.texto)
