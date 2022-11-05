from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='photos/products')
    

    def __str__(self):
        return self.image
