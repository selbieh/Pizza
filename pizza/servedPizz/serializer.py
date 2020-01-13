from rest_framework import serializers
from .models import servedPizza


class servedPizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model=servedPizza
        fields = '__all__'