from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import order,orderPizzaItem




class orderObjectsSerializer(ModelSerializer):

    id=serializers.IntegerField(required=False)


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
        old_pizza_items=instance.orderObjects.all()
        old_pizza_items_id=[item.id for item in  old_pizza_items]
        new_order_list = []
        orderPizzaItem.objects.filter(id__in=old_pizza_items_id).delete()
        for item in orderObjectLists:
            item.pop('id')
            item=orderPizzaItem.objects.create(**item)
            new_order_list.append(item)
        instance.save()
        instance.orderObjects.set(new_order_list)
        return instance







