from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    
class GPU(models.Model):
    model=models.CharField(max_length=100)
    name=models.IntegerField()
    VRAM = models.IntegerField()

    def __str__(self):
        return f"Model:{self.model} Name:{self.name} VRAM:{self.VRAM}"
    

    
