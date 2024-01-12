from django.db import models

class Emoji(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)  # Stocker le symbole de l'emoji (ex. 😀)

    def __str__(self):
        return self.name