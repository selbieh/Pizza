from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import order
from .serializer import orderReadOnlySerializer
from rest_framework.response import Response

class orderViwes(ModelViewSet):
    queryset = order.objects.all()
    serializer_class = orderReadOnlySerializer

    #exampel filter by custumerName
    def get_queryset(self):
        params=self.request.query_params.dict()

        if params == {}:
            return self.queryset
        else:
            #dynamic filter example http://127.0.0.1:8000/orderViwes/?custumerName=sayed&delivery=True

            return self.queryset.filter(**params)

    #overide update to validate order srtatus
    def update(self,  request, pk=None):
        response = super(orderViwes,self).update(request, pk=None)

        the_order=order.objects.get(id=pk)
        if not the_order.delivery:
            return response
        else:
            return Response({'message':'order in delevery process'})







