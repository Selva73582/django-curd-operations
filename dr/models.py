from django.db import models

# Create your models here.

class Drink(models.Model):
    name=models.CharField(max_length=20)
    decription=models.TextField()

    def __str__(self) -> str:
        return self.name