from django.db import models
from servedPizz.models import servedPizza
from django.contrib.auth.models import User














class orderPizzaItem(models.Model):
    sizeChoices = [
        ('medium', 'medium'),
        ('small', 'small'),
        ('large', 'large'),

    ]
    number=models.IntegerField(default=1,blank=True)
    pizza=models.ForeignKey(servedPizza,blank=False,null=True,on_delete=models.SET_NULL)
    size=models.CharField(choices=sizeChoices,max_length=10)
    def __str__(self):
        return self.pizza.name





class order(models.Model):
    custumerName=models.CharField(max_length=65,blank=False)
    fullAdress=models.CharField(max_length=255,blank=False)
    delivery=models.BooleanField(default=False)
    orderObjects=models.ManyToManyField(orderPizzaItem,blank=False)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.custumerName
