from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField('Название товара',max_length=150)
    description = models.TextField('Описание товара')
    parametrs = None
