from django.db import models

# Create your models here.

class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zipcode = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.First_name} {self.Last_name}"
