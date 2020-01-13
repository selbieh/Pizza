from django.urls import path
from .views import orderViwes
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'orderViwes', orderViwes, basename='orderViwes')

urlpatterns=router.urls