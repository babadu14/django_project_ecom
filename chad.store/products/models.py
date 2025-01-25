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