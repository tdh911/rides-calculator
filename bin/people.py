import re

class Person:
    def __init__(self, first, last, area, phone, email, earliest_departure):
        self.first = first
        self.last = last
        self.area = area
        self.phone = phone
        self.email = email
        # Time will be represented as a float
        self.earliest_departure = self._attempt_to_parse_time(earliest_departure.strip())
        self.raw_time = earliest_departure

    # Time represented as a float
    # e.g. 12PM = 12.0, 1PM = 13.0, 1:30PM = 13.5
    def _attempt_to_parse_time(self, departure_time):
        # Match explicit AM times in form HH:MM
        m = re.match(r"(?P<hour>\d{1,2}):?(?P<minute>\d{2})(\s?AM).*?", departure_time, re.IGNORECASE)
        if m:
            hour = float(m.group("hour"))
            minute = float(m.group("minute")) / 60
            return hour + minute
        # Match explicit AM times in form HH
        m = re.match(r"(?P<hour>\d{1,2})(\s?AM).*?", departure_time, re.IGNORECASE)
        if m:
            hour = float(m.group("hour"))
            return hour
        # Match HH:MM, assume PM
        m = re.match(r"(?P<hour>\d{1,2}):?(?P<minute>\d{2}).*?", departure_time)
        if m:
            hour = float(m.group("hour"))
            if hour < 12:
                hour += 12
            minute = float(m.group("minute")) / 60
            return hour + minute
        # Match HH, assume PM
        m = re.match(r"(?P<hour>\d{1,2}).*?", departure_time)
        if m:
            hour = float(m.group("hour"))
            if hour < 12:
                hour += 12
            return hour 

        # Assume 12PM if no match has been made
        return 12.0

         
