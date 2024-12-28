from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)  
    description = models.TextField()  

    def __str__(self):
        return self.title  

class Ingredient(models.Model):
    UNITS = [
        ('gr', 'граммы'),
        ('kg', 'килограммы'),
        ('ml', 'миллилитры'),
        ('l', 'литры'),
        ('pcs', 'штук'),
    ]

    name = models.CharField(max_length=200)  
    quantity = models.FloatField()  
    unit = models.CharField(max_length=10, choices=UNITS) 
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')  

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"  

