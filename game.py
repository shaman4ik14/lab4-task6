"""Initialize all classes for main loop"""


class Room(object):
    def __init__(self, name, description=''):
        self.linked_room = set()
        self.__name = name
        self.description = description
        self.enemies = set()
        self.items = set()

    def set_description(self, new_description):
        self.description = new_description

    def link_room(self, next_room, direction):
        if direction in ['south', 'north', 'west', 'east']:
            if direction == 'south':
                new_direction = 'north'
            elif direction == 'north':
                new_direction = 'south'
            elif direction == 'west':
                new_direction = 'east'
            else:
                new_direction = 'west'
            exist = False
            for places in self.linked_room:
                if places[1] == direction:
                    exist = True
                    break
            if not exist:
                for locations in next_room.linked_room:
                    if locations[1] == new_direction:
                        exist = True
                        break
            if not exist:
                self.linked_room.add((next_room, direction))
                next_room.linked_room.add((self, new_direction))
            else:
                print('Room in this direction has already existed')
        else:
            print('Direction is wrong')

    def set_character(self, other):
        self.enemies.add(other)

    def set_item(self, item):
        self.items.add(item)

    def del_item(self, name):
        self.items.discard(name)

    def get_details(self):
        string = f'{self.__name}\n' \
                 f'--------------------\n' \
                 f'{self.description}\n'
        if self.linked_room:
            for locations in self.linked_room:
                string += f'The {locations[0].__name} is {locations[1]}\n'
        if self.enemies:
            for enemy in self.enemies:
                string += f'{enemy.name} is here!\n{enemy.description}\n'
        if self.items:
            for item in self.items:
                string += f'The [{item.name}] is here - {self.description}'
        if string[-1] == '\n':
            string = string[:-1]
        print(string)

    def get_character(self):
        if len(self.enemies) != 0:
            return list(self.enemies)[0]

    def get_item(self):
        if len(self.items) != 0:
            return list(self.items)[0]

    def move(self, direction):
        for elements in self.linked_room:
            if elements[1] == direction:
                return elements[0]

    def __str__(self):
        return f'Room name: {self.__name}\nDescription: {self.description}\n' \
               f'Linked with: {self.linked_room}\nEnemies: {self.enemies}\nItems: {self.items}'

    def __repr__(self):
        return self.__name
        # return f'Room name: {self.__name}\nDescription: {self.description}\nLinked with: {self.linked_room}'


class Person:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Enemy(Person):
    defeated = 0

    def __init__(self, name, description=''):
        super().__init__(name, description)

    def set_conversation(self, message):
        self.conversation = message

    def set_weakness(self, weakness):
        self.weakness = weakness

    def talk(self):
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self, item):
        if item == self.weakness:
            self.defeated += 1
            return True
        else:
            return False

    def get_defeated(self):
        return self.defeated

    def describe(self):
        return self.description

    def __str__(self):
        return f"Enemy name: {self.name}\n" \
               f"Conversation: {self.conversation}\n" \
               f"Weakness: {self.weakness}\n"

    def __repr__(self):
        return self.name


class Item:
    def __init__(self, name, description=''):
        self.name = name
        self.description = description

    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name

    def describe(self):
        return self.description

    def __str__(self):
        return f'Name: {self.name}\nDescription: {self.description}'

    def __repr__(self):
        return self.name
