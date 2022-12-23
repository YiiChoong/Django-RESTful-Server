from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cars', views.CarViewSet)
router.register(r'trucks', views.TruckViewSet)
router.register(r'boats', views.BoatViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('login/', views.login),
]