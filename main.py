import sys
from hilbert import HilbertsHotel 
def print_menu():
    print("\nHilbert's Hotel Management System")
    print("1. Add guests")
    print("2. Add room manually")
    print("3. Remove room manually")
    print("4. Sort rooms")
    print("5. Find room")
    print("6. Count empty rooms")
    print("7. Write data to file")
    print("8. Display memory usage")
    print("9. Exit")

def main():
    hotel = HilbertsHotel()

    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            channel = int(input("Enter channel number: "))
            num_guests = int(input("Enter number of guests to add: "))
            time_taken = hotel.add_guests(channel, num_guests)
            print(f"Added {num_guests} guests from channel {channel}. Time taken: {time_taken:.6f} seconds")

        elif choice == '2':
            room_number = int(input("Enter room number: "))
            channel_info = input("Enter channel info: ")
            time_taken = hotel.add_room_manual(room_number, channel_info)
            print(f"Added room {room_number} manually. Time taken: {time_taken:.6f} seconds")

        elif choice == '3':
            room_number = int(input("Enter room number to remove: "))
            time_taken = hotel.remove_room_manual(room_number)
            print(f"Removed room {room_number} manually. Time taken: {time_taken:.6f} seconds")

        elif choice == '4':
            time_taken = hotel.sort_rooms()
            print(f"Sorted rooms. Time taken: {time_taken:.6f} seconds")

        elif choice == '5':
            room_number = int(input("Enter room number to find: "))
            room_info, time_taken = hotel.find_room(room_number)
            print(f"Room {room_number} info: {room_info}. Time taken: {time_taken:.6f} seconds")

        elif choice == '6':
            empty_rooms, time_taken = hotel.count_empty_rooms()
            print(f"Number of empty rooms: {empty_rooms}. Time taken: {time_taken:.6f} seconds")

        elif choice == '7':
            filename = input("Enter filename to write data: ")
            time_taken = hotel.write_to_file(filename)
            print(f"Wrote data to file '{filename}'. Time taken: {time_taken:.6f} seconds")

        elif choice == '8':
            memory_used = hotel.memory_usage()
            print(f"Memory used: {memory_used} bytes")

        elif choice == '9':
            print("EXIT!")
            sys.exit(0)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()