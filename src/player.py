# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, current_room, items):
        self.current_room = current_room
        self.items = items