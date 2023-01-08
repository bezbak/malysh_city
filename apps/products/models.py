from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=70
    )
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(
        max_length=100
    )
    image = models.FileField(
        upload_to='product_image/'
    )
    description = models.CharField(
        max_length=255
    )
    sale = models.BooleanField(
        default= False
    )
    price = models.IntegerField(
    )
    sale_price = models.IntegerField(
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        related_name='category',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
