from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import order,orderPizzaItem




class orderObjectsSerializer(ModelSerializer):


    class Meta:
        fields = ['id','pizza','number','size']
        model = orderPizzaItem



class orderReadOnlySerializer(ModelSerializer):
    orderObjects=orderObjectsSerializer(many=True)

    class Meta:
        fields=['orderObjects','custumerName','fullAdress','delivery','id']
        model=order


    def create(self, validated_data):
        orderItems = validated_data.pop('orderObjects')
        the_order = order.objects.create(**validated_data)

        for orderItem in orderItems:
            orderItem = orderPizzaItem.objects.create(**orderItem)
            the_order.orderObjects.add(orderItem)
        return the_order

    def update(self, instance, validated_data):

        orderObjectLists=validated_data.pop('orderObjects')
        instance.custumerName=validated_data.get('custumerName',instance.custumerName)
        instance.fullAdress=validated_data.get('fullAdress',instance.fullAdress)

        new_order_list = []
        for item in orderObjectLists :
            create_item,created=orderPizzaItem.objects.get_or_create(**item)
            new_order_list.append(create_item)
        instance.orderObjects.set(new_order_list)
        return instance







