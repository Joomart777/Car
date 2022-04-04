from django.shortcuts import render

# Create your views here.
from rest_framework.generics import *

from car_app.models import Car
from car_app.serializers import CarSerializer


class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarCreateView(CreateAPIView):
    serializer_class = CarSerializer

class CarUpdateView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetailView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDeleteView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer