from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CarSerializer, TruckSerializer, BoatSerializer
from .models import Car, Truck, Boat

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('id')
    serializer_class = CarSerializer

class TruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all().order_by('id')
    serializer_class = TruckSerializer

class BoatViewSet(viewsets.ModelViewSet):
    queryset = Boat.objects.all().order_by('id')
    serializer_class = BoatSerializer

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        print(username, password)
        return Response({"error": 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
        
    user = authenticate(username = username, password = password)

    if not user:
        return Response({"error": 'Invalid credential'}, status=HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({'token': token.key}, status=HTTP_200_OK)