# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return f"Name: {self.name} - Desc: {self.desc}"

    def __str__(self):
        return f"You are at a {self.name}\n{self.desc}\n\n"
