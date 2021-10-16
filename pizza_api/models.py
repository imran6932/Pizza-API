from django.db import models


class Pizza(models.Model):
    """
    pizza model class created to store data about pizza

    """
    pizza_type = models.CharField(max_length=50)
    pizza_size = models.CharField(max_length=50) 
    toppings = models.CharField(max_length=50)

    def __str__(self):
        return self.pizza_type