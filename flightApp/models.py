from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# Create your models here.

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    operating_airlines = models.CharField(max_length=20)
    departure_city = models.CharField(max_length=20)
    arrival_city = models.CharField(max_length=20)
    date_of_departure = models.DateField()
    estimated_time_of_departure = models.TimeField()

    def get_flight(self):
        return self.flight_number + ' from ' + self.departure_city + ' to ' + self.arrival_city


class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10)


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    Passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def CreateAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
