class Car:
    def __init__(self, driver, seats):
        self.driver = driver
        self.seats = seats
        self.passengers = []
        self.passengers.append(driver)
        self.is_full = seats == 1
        self.departure_time = driver.earliest_departure

    def add_person(self, person):
        if self.is_full:
            return False
        
        if person.earliest_departure > self.departure_time:
            self.departure_time = person.earliest_departure

        self.passengers.append(person)
        self.is_full = self.seats == len(self.passengers)
        return True


