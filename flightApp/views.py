from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view




@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(arrival_city=request.data['arrival_city'], departure_city=request.data['departure_city'], date_of_departure=request.data['date_of_departure'])
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
