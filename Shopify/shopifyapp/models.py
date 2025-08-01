from django.db import models
from userapp.models import User

# Create your models here.
class Category (models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()
    original_price = models.FloatField()
    discount_percentage = models.IntegerField()
    selling_price = models.FloatField()
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}"  
    