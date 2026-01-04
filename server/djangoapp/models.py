from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add any other fields you would like for a car make

    def __str__(self):
        return self.name  # Returns the name of the make


class CarModel(models.Model):
    # Many-to-One relationship to CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    
    # Dealer ID referring to a dealer in the database
    dealer_id = models.IntegerField()
    
    # Choice for Car Type
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as needed
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    
    # Year with validators to restrict range
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])

    def __str__(self):
        return f"{self.car_make.name} {self.name}" # Returns make and model