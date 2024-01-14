from django.db import models

# Create your models here.
class Customer(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=32)
    address = models.TextField(max_length=128, blank=True)

    def __str__(self):
        return f"{self.first} {self.last} {self.phone} {self.email} {self.address}"

class Products(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    typeName = models.CharField(max_length=64, blank=False)              #Which Plant
    categories = models.CharField(max_length=64, blank=False)    
    tag = models.CharField(max_length=64)                                #Search name
    quantity = models.IntegerField()                                     #Product Available we have

    def __str__(self):
        return f"{self.id}: {self.name} the Price {self.price} type {self.typeName} in {self.categories} and the tags are {self.tag} and still available {self.quantity}"

class Card(models.Model):
    cards = models.CharField(max_length=64)                              #Payment way

    def __str__(self):
        return f"Online Payment way {self.cards}"

class MethodToPay(models.Model):
    way = models.CharField(max_length=64)      #If it's "Cash on delivery" or "Online Payment"

    def __str__(self):
        return f"Is it {self.way}"

class Reciver(models.Model):
    name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="User")
    DeliveryWay = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="PaymentWay")
    cart = models.ForeignKey(MethodToPay, on_delete=models.CASCADE, related_name="AddCart")   
    def __str__(self):
        return f"{self.name} will deliver in {self.DeliveryWay}"

class Order(models.Model):
    Name = models.ForeignKey(Reciver, on_delete=models.CASCADE, related_name="User")
    ProductName = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="Plant")
    OrderDate = models.DateTimeField()
    CheckOut = models.IntegerField()             #Quantity of Ordered Plant

    def __str__(self):
        return f"{self.Name}: ordered {self.ProductName} on {self.OrderDate} and the Quantity {self.CheckOut}"

class Payment(models.Model):
    Ammount = models.FloatField()               #Total amount
    PaymentWay = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="PaymentMethod")
    UserID = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="PaymentAccount")

    def __str__(self):
        return f"{self.UserID} have to pay {self.Ammount} by {self.PaymentWay}"

class Employee(models.Model):
    SeName = models.CharField(max_length=64)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=32)
    AccountNumber = models.CharField(max_length=32)    #Employee ID

    def __str__(self):
        return f"{self.SeName} ({self.phone}) {self.email} {self.AccountNumber}"