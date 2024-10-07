# Hilbert's Hotel Problem🏨



## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Performance Optimizations](#performance-optimizations)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is an implementation of the famous thought experiment proposed by mathematician David Hilbert. In this paradoxical hotel, we can accommodate infinitely many guests in infinitely many rooms, even when the hotel is "full"!

Our system provides an efficient and optimized solution to manage this infinite hotel, leveraging advanced data structures and algorithms to handle an astronomical number of rooms and guests.

## Features

- 🏃‍♂️ Lightning-fast guest check-in and check-out
- 🔍 Efficient room lookup and management
- 🔢 Infinite room capacity
- 📊 Real-time occupancy statistics
- 💾 Memory-efficient data storage
- 📝 Data persistence and file I/O operations
- ⏱️ Performance metrics for all operations

## Technologies Used

- Python 3.10+
- Custom AVL Tree implementation
- Memory-mapped file storage
- Parallel processing for bulk operations

## Installation

1. Clone the repository:
   ```
   git clone <link>
   cd hilberts-hotel
   ```

## Usage

To run the Hilbert's Hotel Management System:

```
python main.py
```

Follow the on-screen prompts to interact with the system. You can:

- Add guests to the hotel
- Manually add or remove specific rooms
- Find room information
- Count empty rooms
- Sort rooms (although they're always sorted!)
- Write hotel data to a file
- Check memory usage

## Performance Optimizations

Our system employs several optimizations to ensure top-notch performance:

1. **Custom AVL Tree**: A self-balancing binary search tree for O(log n) operations.
2. **Memory-Mapped Files**: Efficient handling of large datasets that exceed available RAM.
3. **Parallel Processing**: Utilizes multiple CPU cores for bulk operations.
4. **Constant-Time Sorting**: The AVL tree structure ensures data is always sorted.

