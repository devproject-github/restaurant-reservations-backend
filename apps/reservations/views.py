from rest_framework import viewsets
from apps.reservations.models import (Area, Rating, Reservation,
                     Restaurant, Table, TableAvailability, Turn)
from apps.reservations.serializers import (AreaSerializer, RatingSerializer,
                          ReservationsSerializer, RestaurantSerializer,
                          TableSerializer, TableAvailabilitySerializer, TurnSerializer)
from apps.customers.models import Customer
from apps.customers.serializers import CustomerSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationsSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = TableAvailability.objects.all()
    serializer_class = TableAvailabilitySerializer


class TurnViewSet(viewsets.ModelViewSet):
    queryset = Turn.objects.all()
    serializer_class = TurnSerializer