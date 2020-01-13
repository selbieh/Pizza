from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import servedPizza
from .serializer import servedPizzaSerializer
from django.shortcuts import get_object_or_404




class servedPizzaView(ViewSet):
    queryset=servedPizza.objects.all()
    serializer=servedPizzaSerializer

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset =self.queryset
        pizza = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer(pizza)
        return Response(serializer.data)



