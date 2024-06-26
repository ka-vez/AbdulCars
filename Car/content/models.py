from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    images = models.ImageField( upload_to='brand images/', blank=True, null=True)
    slug = models.SlugField (unique=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField('Car Name', max_length=50)
    description = models.TextField()
    images = models.ImageField(upload_to='car images/', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    slug = models.SlugField (unique=True)
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name
