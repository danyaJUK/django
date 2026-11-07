from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    country = models.CharField(verbose_name='страна')
    name = models.CharField(verbose_name='название')

class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(verbose_name="Цена", max_digits=10)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Производитель")