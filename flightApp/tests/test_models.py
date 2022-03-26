from django.test import TestCase
from flightApp.models import *



class FlightTest(TestCase):
    """Test module for flight model"""
    def setUp(self):
        Flight.objects.create(
            flight_number = '2141930',
            operating_airlines = 'Indian airlines',
            departure_city = 'Kolkata',
            arrival_city = 'Lucknow',
            date_of_departure = "2022-03-23",
            estimated_time_of_departure = "14:29:00",
            )
        Flight.objects.create(
            flight_number = '2141830',
            operating_airlines = 'American airlines',
            departure_city = 'Austin',
            arrival_city = 'London',
            date_of_departure = "2022-03-23",
            estimated_time_of_departure = "14:29:00",
            )
    def test_flight_info(self):
        flight_Indian = Flight.objects.get(flight_number='2141930')
        flight_American = Flight.objects.get(flight_number='2141830')
        self.assertEqual(
            flight_Indian.get_flight(), "2141930 from Kolkata to Lucknow"
        )
        self.assertEqual(
            flight_American.get_flight(), "2141830 from Austin to London"
        )
