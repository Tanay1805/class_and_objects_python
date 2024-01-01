from datetime import datetime, timedelta

class Room:
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity = capacity
        self.reservations = []

    def is_available(self, start_time, end_time):
        for reservation in self.reservations:
            if start_time < reservation['end_time'] and end_time > reservation['start_time']:
                return False
        return True

    def book_room(self, user, start_time, end_time):
        if self.is_available(start_time, end_time):
            reservation = {'user': user, 'start_time': start_time, 'end_time': end_time}
            self.reservations.append(reservation)
            print(f"Room {self.room_id} booked by {user.name} from {start_time} to {end_time}")
            return True
        else:
            print(f"Room {self.room_id} is not available at the specified time.")
            return False

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class ConferenceRoomBookingSystem:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room_id, capacity):
        if room_id not in self.rooms:
            self.rooms[room_id] = Room(room_id, capacity)
            print(f"Room {room_id} added to the system with capacity {capacity}.")
        else:
            print(f"Room {room_id} already exists in the system.")

    def check_room_availability(self, room_id, start_time, end_time):
        if room_id in self.rooms:
            return self.rooms[room_id].is_available(start_time, end_time)
        else:
            print(f"Room {room_id} does not exist in the system.")
            return False

    def book_room(self, room_id, user, start_time, end_time):
        if room_id in self.rooms:
            return self.rooms[room_id].book_room(user, start_time, end_time)
        else:
            print(f"Room {room_id} does not exist in the system.")
            return False

# Example Usage with User Input:
booking_system = ConferenceRoomBookingSystem()

while True:
    print("\n1. Add Room\n2. Check Room Availability\n3. Book Room\n4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        room_id = input("Enter Room ID: ")
        capacity = int(input("Enter Room Capacity: "))
        booking_system.add_room(room_id, capacity)
    elif choice == '2':
        room_id = input("Enter Room ID: ")
        start_time = datetime.fromisoformat(input("Enter Start Time (YYYY-MM-DD HH:MM): "))
        end_time = datetime.fromisoformat(input("Enter End Time (YYYY-MM-DD HH:MM): "))
        if booking_system.check_room_availability(room_id, start_time, end_time):
            print(f"Room {room_id} is available at the specified time.")
        else:
            print(f"Room {room_id} is not available at the specified time.")
    elif choice == '3':
        room_id = input("Enter Room ID: ")
        user_name = input("Enter Your Name: ")
        user_email = input("Enter Your Email: ")
        user = User(1, user_name, user_email)
        start_time = datetime.fromisoformat(input("Enter Start Time (YYYY-MM-DD HH:MM): "))
        end_time = datetime.fromisoformat(input("Enter End Time (YYYY-MM-DD HH:MM): "))
        booking_system.book_room(room_id, user, start_time, end_time)
    elif choice == '4':
        break
    else:
        print("Invalid Choice. Please enter a valid option.")
