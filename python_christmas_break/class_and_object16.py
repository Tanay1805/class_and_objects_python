class Room:
    def __init__(self, room_number, capacity, rate_per_night):
        self.room_number = room_number
        self.capacity = capacity
        self.rate_per_night = rate_per_night
        self.is_booked = False

    def display(self):
        print(f"Room {self.room_number} - Capacity: {self.capacity} people, Rate per night: ${self.rate_per_night}")

    def book(self):
        self.is_booked = True
        print(f"Room {self.room_number} booked successfully.")


class Guest:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print(f"Guest: {self.name} - Email: {self.email}")


class Reservation:
    def __init__(self, guest, room, nights):
        self.guest = guest
        self.room = room
        self.nights = nights

    def calculate_total_cost(self):
        return self.room.rate_per_night * self.nights

    def generate_invoice(self):
        print("Invoice:")
        self.guest.display()
        self.room.display()
        print(f"Nights: {self.nights}")
        total_cost = self.calculate_total_cost()
        print(f"Total Cost: ${total_cost}")


class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        self.reservations = []

    def display_available_rooms(self):
        print("Available Rooms:")
        for room in self.rooms:
            if not room.is_booked:
                room.display()

    def book_room(self, guest, room_number, nights):
        for room in self.rooms:
            if room.room_number == room_number and not room.is_booked:
                room.book()
                reservation = Reservation(guest, room, nights)
                self.reservations.append(reservation)
                return reservation
        print(f"Room {room_number} is not available or does not exist.")
        return None


if __name__ == "__main__":
 
    room1 = Room(101, 2, 100)
    room2 = Room(102, 4, 150)
    room3 = Room(103, 1, 80)

    hotel = Hotel("Comfort Inn", [room1, room2, room3])


    guest_name = input("Enter your name: ")
    guest_email = input("Enter your email: ")
    guest = Guest(guest_name, guest_email)


    hotel.display_available_rooms()

    room_number = int(input("Enter the room number you want to book: "))
    nights = int(input("Enter the number of nights: "))

    reservation = hotel.book_room(guest, room_number, nights)
    if reservation:
        reservation.generate_invoice()
