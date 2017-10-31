class Person:
    def __init__(self, first, last, area, phone, email, earliest_departure):
        self.first = first
        self.last = last
        self.area = area
        self.phone = phone
        self.email = email
        self.earliest_departure = _attempt_to_parse_time(earliest_departure)

    # TODO: Parse time into a comparable object
    def _attempt_to_parse_time(departure_time):
        return departure_time
