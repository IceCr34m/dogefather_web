from django.db import models

# Create your models here.


class TokenData(models.Model):
    symbol = models.CharField(max_length=50, null=False,
                              blank=False, unique=True)
    current_price = models.CharField(max_length=200, null=True, blank=True)
    market_cap = models.CharField(max_length=23, null=True, blank=True)

