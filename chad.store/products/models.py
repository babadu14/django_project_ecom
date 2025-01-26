from django.db import models
from products.choices import Currency
from config.util_models.models import TimeStampModel
from django.core.validators import MaxValueValidator

# Create your models here.


class Product(TimeStampModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    currency = models.CharField(max_length=255, choices=Currency.choices, default= Currency.GEL)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
    

class ProductTag(TimeStampModel):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField('products.Product', related_name='product_tags')

    def __str__(self):
        return self.name

class Review(TimeStampModel):
    user = models.ForeignKey('users.User', 
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True,
                             related_name='reviews')
    product = models.ForeignKey('products.Product', 
                                on_delete=models.CASCADE, 
                                related_name='reviews')
    content = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    def __str__(self):
        return f'written by: {self.user}'


class Cart(TimeStampModel):
    products = models.ManyToManyField('products.Product', related_name='carts')
    users = models.OneToOneField('users.User', related_name='cart', on_delete=models.CASCADE)


class FavoriteProduct(TimeStampModel):
    products = models.ForeignKey('products.Product',
                                 related_name='favorite_products',
                                 on_delete=models.CASCADE)
    
    user = models.ForeignKey('users.User',
                             related_name='favorite_products',
                             on_delete=models.SET_NULL,
                             null = True,
                             blank=True)
    
class ProductImage(TimeStampModel):
    product = models.ForeignKey('products.Product', 
                                related_name='images',
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')