from datetime import datetime, date
import json
import sys
from coefficients import *


class RegularTicket:
    """Class for regular ticket."""
    def __init__(self, num: int, title: str, price: float, event_date: date):
        self.num = num
        self.title = title
        self.price = price
        self.date = event_date
        self.__purchased_date = date.today().strftime("%d.%m.%Y")

    def __str__(self):
        return f"Ticket {self.num} \"{self.title}\", {self.date}, {self.price} uah"

    def __iter__(self):
        for key, value in self.__dict__.items():
            key = str(key).removeprefix("_RegularTicket__")
            yield key, value

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        if not isinstance(num, int):
            raise TypeError("Number of ticket must be int")
        if not num > 0:
            raise ValueError("Number must be bigger than zero")
        self.__num = num

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title of event must be string")
        if not title:
            raise ValueError("Title cannot be empty")
        self.__title = title

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise TypeError("Price of ticket must be float")
        if not price > 0:
            raise ValueError("Price must be bigger than zero")
        self.__price = price

    @property
    def event_date(self):
        return self.__event_date

    @event_date.setter
    def event_date(self, event_date):
        if not isinstance(event_date, str):
            raise TypeError("the event date must be a string")
        try:
            datetime.strptime(event_date, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Incorrect date format, should be DD.MM.YYYY")
        self.__event_date = event_date

    @property
    def purchased_date(self):
        return self.__purchased_date


class AdvanceTicket(RegularTicket):
    """Class for advance ticket (60 or more days)."""
    def __init__(self, num: int, title: str, price: float, event_date: date):
        super().__init__(num, title, price * COEFF_ADVANCE, event_date)


class LateTicket(RegularTicket):
    """Class for late ticket (10 or less days)."""
    def __init__(self, num: int, title: str, price: float, event_date: date):
        super().__init__(num, title, price * COEFF_LATE, event_date)


class StudentTicket(RegularTicket):
    """Class for student ticket."""
    def __init__(self, num: int, title: str, price: float, event_date: date):
        super().__init__(num, title, price * COEFF_STUDENT, event_date)


def buy_ticket(is_student=False):
    with open("events.json") as events_file:
        events = json.load(events_file)

    today = datetime.today()

    i = 1
    for event in events:
        print(i, ": ", event["title"], event["date"], event["price"], "uah")
        i += 1

    number = 0
    while True:
        try:
            number = int(input("Enter the number: "))
        except ValueError as error:
            print("Error:", error)
            continue

        if not 0 <= number <= len(events):
            print("Try again")
            continue
        if not number:
            return
        break

    with open("purchased.json") as purchased_file:
        purchased_tickets = json.load(purchased_file)
    ticket_id = len(purchased_tickets) + 1

    if is_student:
        ticket = StudentTicket(ticket_id, events[ticket_id - 1]["title"],
                               events[ticket_id - 1]["price"], events[ticket_id - 1]["date"])
    else:
        event_date = datetime.strptime(events[number - 1]["date"], "%d.%m.%Y")
        days_before_event = (event_date - today).days

        if days_before_event < 10:
            ticket = LateTicket(ticket_id, events[ticket_id - 1]["title"],
                                events[ticket_id - 1]["price"], events[ticket_id - 1]["date"])
        elif days_before_event >= 60:
            ticket = AdvanceTicket(ticket_id, events[ticket_id - 1]["title"],
                                   events[ticket_id - 1]["price"], events[ticket_id - 1]["date"])
        else:
            ticket = RegularTicket(ticket_id, events[ticket_id - 1]["title"],
                                   events[ticket_id - 1]["price"], events[ticket_id - 1]["date"])

    purchased_tickets.append(dict(ticket))
    with open("purchased.json", "w") as purchased_file:
        json.dump(purchased_tickets, purchased_file, indent=4)

    print(f"Your ticket id: {ticket_id}")


def find_ticket():
    with open("purchased.json") as purchased_file:
        purchased_tickets = json.load(purchased_file)

    while True:
        try:
            ticket_id = int(input("Enter the id of ticket: "))
            break
        except ValueError as error:
            print("Error:", error)

    if 0 < ticket_id <= len(purchased_tickets):
        ticket = purchased_tickets[ticket_id - 1]
        print(f'#{ticket_id}: {ticket["title"]}, {ticket["date"]}, {ticket["price"]}')
    else:
        print("Ticket with such id does not exist")


while True:
    print("\nMenu:\n"
          "1: buy a ticket\n"
          "2: buy a ticket for student\n"
          "3: view my ticket by unique number\n"
          "0: exit")

    while True:
        try:
            option = int(input("Enter the number: "))

            if option == 1:
                buy_ticket()
                break
            elif option == 2:
                buy_ticket(is_student=True)
                break
            elif option == 3:
                find_ticket()
                break
            elif not option:
                print("Bye!")
                sys.exit()
            else:
                print("Try again.")
        except ValueError as error:
            print("Error:", error)
