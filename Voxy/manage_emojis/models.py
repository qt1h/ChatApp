from django.db import models

class Emoji(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)  # Stock the emoji (ex. 😀)

    def __str__(self):
        return self.name