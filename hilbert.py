import sys
import time
import random
import mmap
import os
from concurrent.futures import ProcessPoolExecutor
from avl_tree import AVLTree, AVLNode

class HilbertsHotel:
    def __init__(self):
        self.rooms = AVLTree()
        self.max_room = 0
        self.file_path = "hotel_data.mmap"
        self.mmap_size = 1024 * 1024 * 1024  # 1GB initial size
        self._init_mmap()

    def _init_mmap(self):
        with open(self.file_path, "wb") as f:
            f.write(b'\0' * self.mmap_size)

    def _ensure_mmap_size(self, required_size):
        if required_size > self.mmap_size:
            self.mmap_size = max(self.mmap_size * 2, required_size)
            with open(self.file_path, "r+b") as f:
                f.truncate(self.mmap_size)

    def add_guests(self, channel: int, num_guests: int) -> float:
        start_time = time.time()

        def add_guest(i: int):
            room_number = self.max_room + i + 1
            channel_info = f"no_{channel}_" + "_".join(str(random.randint(1, 5)) for _ in range(5))
            return room_number, channel_info

        with ProcessPoolExecutor() as executor:
            new_rooms = list(executor.map(add_guest, range(num_guests)))

        self._ensure_mmap_size(len(new_rooms) * 100)  # 100 bytes per room entry
        with open(self.file_path, "r+b") as f:
            mm = mmap.mmap(f.fileno(), 0)
            for room_number, channel_info in new_rooms:
                mm.write(f"{room_number},{channel_info}\n".encode())
                self.rooms.insert(room_number, channel_info)
            mm.close()

        self.max_room = max(self.max_room, max(room for room, _ in new_rooms))
        return time.time() - start_time

    def add_room_manual(self, room_number: int, channel_info: str) -> float:
        start_time = time.time()
        if not self.rooms.get(room_number):
            self.rooms.insert(room_number, channel_info)
            self.max_room = max(self.max_room, room_number)
            self._ensure_mmap_size(100)  # 100 bytes per room entry
            with open(self.file_path, "r+b") as f:
                mm = mmap.mmap(f.fileno(), 0)
                mm.seek(0, 2)  # Go to the end of the file
                mm.write(f"{room_number},{channel_info}\n".encode())
                mm.close()
        return time.time() - start_time

    def remove_room_manual(self, room_number: int) -> float:
        start_time = time.time()
        if self.rooms.get(room_number):
            self.rooms.delete(room_number)
            if room_number == self.max_room:
                self.max_room = self.rooms.get_max_key() or 0
        return time.time() - start_time

    def sort_rooms(self) -> float:
        # AVLTree is always sorted, so this operation is O(1)
        return 0.0

    def find_room(self, room_number: int) -> tuple:
        start_time = time.time()
        result = self.rooms.get(room_number) or "Room not found"
        return result, time.time() - start_time

    def count_empty_rooms(self) -> tuple:
        start_time = time.time()
        empty_rooms = self.max_room - len(self.rooms)
        return empty_rooms, time.time() - start_time

    def write_to_file(self, filename: str) -> float:
        start_time = time.time()
        with open(filename, 'w') as f:
            for room, channel_info in self.rooms:
                f.write(f"{room},{channel_info}\n")
        return time.time() - start_time

    def memory_usage(self) -> int:
        return sys.getsizeof(self.rooms) + os.path.getsize(self.file_path)

# def run_tests():
#     hotel = HilbertsHotel()

#     print("Test 1: Adding guests")
#     for channel in range(1, 5):
#         time_taken = hotel.add_guests(channel, 1000000)
#         print(f"Added 1,000,000 guests from channel {channel}. Time taken: {time_taken:.6f} seconds")

#     print("\nTest 2: Manual room operations")
#     time_taken = hotel.add_room_manual(5000000, "no_1_2_3_4_5")
#     print(f"Added room 5,000,000 manually. Time taken: {time_taken:.6f} seconds")
#     time_taken = hotel.remove_room_manual(2500000)
#     print(f"Removed room 2,500,000 manually. Time taken: {time_taken:.6f} seconds")

#     print("\nTest 3: Sorting rooms")
#     time_taken = hotel.sort_rooms()
#     print(f"Sorted rooms. Time taken: {time_taken:.6f} seconds")

#     print("\nTest 4: Finding room")
#     room_info, time_taken = hotel.find_room(1500000)
#     print(f"Room 1,500,000 info: {room_info}. Time taken: {time_taken:.6f} seconds")

#     print("\nTest 5: Counting empty rooms")
#     empty_rooms, time_taken = hotel.count_empty_rooms()
#     print(f"Number of empty rooms: {empty_rooms}. Time taken: {time_taken:.6f} seconds")

#     print("\nTest 6: Writing to file")
#     time_taken = hotel.write_to_file("hotel_data_output.txt")
#     print(f"Wrote data to file. Time taken: {time_taken:.6f} seconds")

#     print("\nTest 7: Memory usage")
#     memory_used = hotel.memory_usage()
#     print(f"Memory used: {memory_used} bytes")

# if __name__ == "__main__":
#     run_tests()