class HotelRoom:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.is_booked = False

    def book_room(self):
        if self.is_booked==False:
            self.is_booked = True
            print(f"Room {self.room_number} is now booked.")
        else:
            print(f"Room {self.room_number} is already booked!")

    def check_availability(self):
        if self.is_booked==True:
            print(f"Room {self.room_number} is currently booked.")
        else:
            print(f"Room {self.room_number} is available.")

    def display_details(self):
        if self.is_booked==True:
            status = "Booked"
        else:
            status = "Available"
        print(f"Room {self.room_number} ({self.room_type}) - {status}")

# Create instances (objects) of HotelRoom class
room1 = HotelRoom(101, "Single")
room2 = HotelRoom(102, "Double")
room3 = HotelRoom(103, "Suite")


print("\n")
room1.display_details()
room1.book_room()
room1.check_availability()
print("\n")
room2.display_details()
room3.display_details()
room2.book_room()
room3.book_room()
print("\n")
room1.display_details()
room2.display_details()
