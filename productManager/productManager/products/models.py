from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    photo = models.ImageField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.name