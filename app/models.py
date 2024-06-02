from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'products'


class Image(models.Model):
    link = models.ImageField(upload_to=settings.MEDIA_ROOT)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    
    class Meta :
        db_table="images"
        