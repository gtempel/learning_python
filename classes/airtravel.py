#! /usr/bin/env python3

'''
Model for aircraft flights
'''


class Flight:
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError(
                "Invalid airline code '{}' (must be upper case)".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(
                "Invalid route number '{}' (must be number 0...9999)".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        # the [None] takes care of "row zero" which doesn't exist so 
        # our indexing is 1:1 with the rows
        # the rest is a dictionary comprehension within the list comprehension
        self._seating = [None] + [ {letter:None for letter in seats} for _ in rows ]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):
        '''parse a seat designator into a valid row and letter

        Args:
            seat: a seat designator, such as '12C'
            passenger: the passenger name as string

        Returns:
            A tuple containing an integer row and a string seat.

        Raises:
            ValueError: if seat is unavailable
        '''
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1] # the 'C' in '12C'
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1] # everthing exclusive of last char; the '12' in '12C'
        try:
            row = int(row_text)
        except ValueError as err:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))
        return row, letter


    def allocate_seat(self, seat, passenger):
        '''Allocate a seat to a passenger

        Args:
            seat: a seat designator, such as '12C'
            passenger: the passenger name as string
        
        Raises:
            ValueError: if seat is unavailable
        '''
        row, letter = self._parse_seat(seat)
        
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} is already occupied".format(seat))
        
        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        '''
        Relocate a passenger to a different seat.

        Args:
            from_seat: The existing seat designator, as '12C'
            to_seat: the new seat designator, as '14F'
        '''
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))
        
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} is already occupied".format(to_seat))
        
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None


    def num_available_seats(self):
        # using two nested generators
        # outer filters for non-none rows
        return sum(sum(1 for s in row.values() if s is None)
                    for row in self._seating if row is not None)

    def _passenger_seats(self):
        '''
        A generator producing an iterable series of passengers and 
        seating allocations on this flight
        '''
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield(passenger, "{}{}".format(row, letter))


    def make_boarding_cards(self, card_printer):
        '''
        invoke this method by passing the console_card_printer method
        as an argument/parameter to the method, as in:
        
        flight.make_boarding_cards(console_card_printer)
        '''
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())


class Aircraft:
    def __init__(self, registration):
        self._registration = registration
    
    def registration(self):
        return self._registration

    def num_seats(self):
        # self doesn't exist here, but will in the sub classes
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):
    def model(self):
        return "Airbus A319"
    
    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):
    def model(self):
        return "Boeing 777"
    
    def seating_plan(self):
        return range(1, 35), "ABCDEFGHJK"


def make_flight():
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat('12C', "George Tempel")
    f.allocate_seat('2F', 'Emmet')
    f.relocate_passenger('12C', '2E')
    return f

def console_card_printer(passenger, seat, flight_number, aircraft):
    '''
    A module-method to print boarding passes. 
    Instead of building this logic into the Flight, which doesn't quite
    make sense, we're going to follow the "tell, don't ask" approach.
    '''
    output = "| Name: {0}" \
             "  Flight: {1}" \
             "  Seat: {2}" \
             "  Aircraft: {3}" \
             " |".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()
