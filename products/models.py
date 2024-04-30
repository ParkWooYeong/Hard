from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    my_datetime = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title