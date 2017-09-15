from django.db import models

# Create your models here.

class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    describe = models.CharField(max_length=500, default='')
    price = models.FloatField()
    isDelete = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)