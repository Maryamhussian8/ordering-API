from django.db import models

class Meals(models.Model):
    name= models.CharField(max_length=55)
    description = models.TextField()
    price= models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    