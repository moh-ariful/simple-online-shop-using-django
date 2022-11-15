from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=201)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=201)
    description = models.TextField(max_length=799)
    image = models.CharField(max_length=301)

    def __str__(self):
        return self.title