from django.db import models

# Create your models here.
# Model and structure basic of produuct

class Product(models.Model):
    name = models.CharField(max_length=200)
    shortDescription = models.TextField()
    price = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now=False, auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True, auto_now_add=False)



    def __str__(self):
        return self.name