class Car:
    def __init__(self, driver, seats):
        self.driver = driver
        self.seats = seats
        self.passengers = []
        self.passengers.append(driver)
        self.is_full = seats == 1
        self.departure_time = driver.earliest_departure

    def add_person(self, person):
        if is_full:
            return None
        
        # TODO: Properly implement time
        if person.earliest_departure > self.departure_time:
            self.departure_time = person.earliest_departure

        return self.departure_time


