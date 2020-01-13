from django.db import models


class servedPizza(models.Model):
    typeChoices=[
    ('meet', 'meet'),
    ('cheese', 'cheese'),
    ('chicken', 'chicken'),

]
    name=models.CharField(max_length=255,blank=False)
    type=models.CharField(choices=typeChoices,max_length=15)

    def __str__(self):
        return self.name

# Create your models here.
