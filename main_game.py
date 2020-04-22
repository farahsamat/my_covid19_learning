from src.room import Room
from src.character import Enemy

# create rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining = Room("Dining")
dining.set_description("Where family sit together and have meals.")

living = Room('Living')
living.set_description("A room where TV, game console, music instruments, mini library, play corner and a BIG couch sit")

hallway = Room("Hallway")
hallway.set_description("Mini gallery that leads you to the powder room.")

powder_room = Room("Powder room")
powder_room.set_description("You can do your private businesses here.")

# link rooms
kitchen.link_room(dining, "north")
kitchen.link_room(hallway, "east")
dining.link_room(kitchen, "south")
dining.link_room(living, "east")
living.link_room(hallway, "south")
living.link_room(dining, "west")
hallway.link_room(living, "north")
hallway.link_room(powder_room, "south")
hallway.link_room(kitchen, "west")
powder_room.link_room(hallway, "north")

# characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brainnnnnnns....")
dave.set_weakness("cheese")

zombot = Enemy("Zombot", "A hi-tech zombie that is made of metal")
zombot.set_weakness("water")

# place a character in room
dining.set_character(dave)
hallway.set_character(zombot)

# move around
current_room = dining
dead = False

while dead is False:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character() #check character
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "fight":
        print("What will you fight with?")
        weapon = input()
        if inhabitant.fight(weapon) == True:
            current_room.remove_character()
        else:
            print("***Game over***")
            dead = True






