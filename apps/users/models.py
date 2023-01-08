from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.products.models import Product
# Create your models here.
class User(AbstractUser):
    profile_image = models.FileField(
        upload_to="profile_images/",
        blank=True, 
        null=True
    )
    
class Order(models.Model):
    first_name = models.CharField(
        max_length=50
    )
    last_name = models.CharField(
        max_length=50
    )
    adres = models.CharField(
        max_length=100
    )
    city = models.CharField(
        max_length=50
    )
    phone_number = models.CharField(
        max_length=25
    )
    price = models.PositiveIntegerField(
    )
    product = models.ForeignKey(
        Product,
        related_name='product_order',
        on_delete=models.CASCADE
    )
    PRODUCT_STATUS = (
        ('Обговор', 'Обговор'),
        ('Доставка', 'Доставка'),
        ('Доставлено', 'Доставлено'),
        ('Возвращено', 'Возвращено'),
        ('Поменяли', 'Поменяли'),
    )
    status = models.CharField(
        choices=PRODUCT_STATUS,
        default='Обговор',
        max_length=20,
    )
    swipe_product = models.ForeignKey(
        ('products.Product'),
        related_name='product_swipe',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f'{self.first_name}, {self.product.title}'
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'