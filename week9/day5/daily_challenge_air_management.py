import datetime
from typing import List


class Company:
    def __init__(self, company_id: str, name: str, planes: list):
        self.company_id = company_id
        self.name = name
        self.planes = planes

    def add_planes(self, planes):
        self.planes.append(planes)


class Airplane:
    def __init__(self, id: int, current_location: Airport, company: Company, next_flights: list):
        self.id = id
        self.current_location = current_location
        self.company = company
        self.next_flights = next_flights

    def fly(self, destination):
        pass

    def location_on_date(self, date):
        return self.current_location

    def available_on_date(self, date, location):
        if self.current_location == location == self.next_flights is None:
            return True


class Flight:
    def __init__(self, date: datetime, destination: Airport, origin: Airport, plane: Airplane, id: str):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = id

    def take_off(self):
        pass

    def land(self, destination):
        Airplane.current_location = destination


class Airport:
    def __init__(self, city: str, planes: list, scheduled_flights: list, scheduled_arrivals:list):
        self.city = city
        self.planes = planes
        self.scheduled_flights = scheduled_flights
        self.scheduled_arrivals = scheduled_arrivals

    def schedule_flight(self, destination, datetime):
        if plane is self.planes:
            if datetime not in plane.next_flights.date:
                new_flight = Flight(datetime, destination, plane.current_location, plane, plane.id)
                plane.next_flights.append(new_flight)

    def info(self, start_date, end_date):
        for flight in self.scheduled_departures:
            if flight.date >= start_date and flight.date <= end_date:
                print(flight.id)