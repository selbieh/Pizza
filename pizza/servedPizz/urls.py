from django.urls import path
from .views import servedPizzaView
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'servedPizzaView', servedPizzaView, basename='servedPizzaView')

urlpatterns=router.urls