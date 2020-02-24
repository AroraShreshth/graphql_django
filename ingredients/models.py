from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    notes=models.TextField()
    
    category=models.ForeignKey(
        Category, 
        related_name='ingredients', 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
    


