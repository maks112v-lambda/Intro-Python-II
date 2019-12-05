# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move_player(self, direction):
        if getattr(self.current_room, direction, None) is not None:
            self.current_room = getattr(self.current_room, direction)
            print("\n===========================\n")
        else:
            print('\n\nInvalid Direction\n\n')
