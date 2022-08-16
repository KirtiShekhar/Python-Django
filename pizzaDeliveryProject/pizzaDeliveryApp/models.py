from django.db import models

# Create your models here.
class PizzaModel(models.Model):
    pizzaName = models.CharField(max_length = 50)
    pizzaPrice = models.CharField(max_length = 10)


class CustomerModel(models.Model):
    customerId = models.CharField(max_length = 10)
    contactNumber = models.CharField(max_length = 10)
    emailAddress = models.CharField(max_length = 50)

class PizzasOrderModel(models.Model):
    customerUsername = models.CharField(max_length = 50)
    customerContactNumber = models.CharField(max_length = 10)
    customerAddress = models.CharField(max_length = 50)
    PizzasOrderedItems = models.CharField(max_length = 10)
    customerStatus = models.CharField(max_length = 10)