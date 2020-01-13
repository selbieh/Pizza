from django.contrib import admin

from .models import orderPizzaItem,order


admin.site.register([orderPizzaItem,order])