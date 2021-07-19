from django.db import models
from django.core.exceptions import ValidationError

def inRange(value):
    if value >= 0 and value <= 500000:
        return value
    else:
        raise ValidationError("Sorry...we do not deliver at this location")

def quantityLimit(value):
    if value > 0 and value <= 1000:
        return value
    else:
        raise ValidationError("Sorry...please enter a valid quantity number")

def priceLimit(value):
    if value > 0 and value <= 100000:
        return value
    else:
        raise ValidationError("Sorry...the price is not in the permissible range")

class itemDetails(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(validators=[quantityLimit])
    price = models.FloatField(validators=[priceLimit])

class offerTypeAndValue(models.Model):
    type = models.CharField(max_length=50)
    offerValue = models.PositiveIntegerField(blank=True, default=0)


class myOrder(models.Model):
    order_items = models.ManyToManyField(itemDetails)
    distance = models.PositiveIntegerField(validators=[inRange])
    offer = models.ManyToManyField(offerTypeAndValue, blank=True)
