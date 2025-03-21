from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=200)
    shipping_phone= models.CharField(max_length=200)
    shipping_email = models.CharField(max_length=200, null=True, blank=True)
    shipping_address1 = models.CharField(max_length=200, null=True, blank=True)
    shipping_address2 = models.CharField(max_length=200, null=True, blank=True)
    shipping_city = models.CharField(max_length=200, null=True, blank=True)
    shipping_zipcode = models.CharField(max_length=200, null=True, blank=True)
    shipping_country = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Shipping Address"

    def __str__(self):
        return f'Shipping Address - {str(self.id)}'
