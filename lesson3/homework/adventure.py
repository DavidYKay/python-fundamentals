# Adventure game spec

"""
Programmer should have the ability to:
    * define room descriptions
    * define room exits
    * define room names

Player should have the ability to:
    * Read room descriptions
    * Walk between rooms
"""

import csv

def print_rooms(rooms):
    """Prints a room to the console. For debugging purposes only."""
    for room in rooms:
        print(room['room_name'])
        print(room['exits'])
        print(room['description'])

def load_rooms():
    """Load the rooms from CSV into a list of Dictionaries"""
    pass

def look(room):
    """Given a Room dictionary, print out the description of the current room and the exits of the current room."""
    pass

def get_room(rooms, name):
    """Given a room name, get the room from the list of rooms."""
    pass

def move(rooms, origin, destination_name):
    """Given the list of rooms, the current room as a dictionary, and the name of the destination,
       return the destination room as a dictionary if it is a valid destination.
       If it is an invalid destination, return None."""
    pass

def get_player_input():
    """Ask the player where they would like to go next."""
    pass

def main():
    """The main loop.
       Initializes the game state, prints the current room, asks for input, handles the input,
       and keeps looping, forever."""
    pass

main()
