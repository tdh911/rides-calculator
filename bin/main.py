from people import Person
from car import Car
import pandas as pd

def main():
    excel_book = raw_input("Type out the excel worksheet filename: ")
    attendees = pd.read_excel(excel_book, sheetname="reg list")

    # Construct unsorted list of cars and general passengers
    cars = []
    passengers = []
    for i in attendees.index:
        first = attendees["first"][i]
        last = attendees["last"][i]
        area = attendees["area"][i]
        email = attendees["email"][i]
        phone = attendees["phone"][i]
        departure_time = attendees["earliest departure time"][i]

        passenger = Person(first, last, area, phone, email, departure_time)
        if not attendees["car seatbelts"][i] == 0:
            seats = attendees["car seatbelts"][i]
            car = Car(passenger, seats)
            cars.append(car)
        else:
            passengers.append(passenger)
            
    # Sort both lists based off departure time

    # Iterate through the lists and add the passengers to the car

    # Write the cars to an excel, special section for unseated passengers

if __name__ == "__main__":
    main()
