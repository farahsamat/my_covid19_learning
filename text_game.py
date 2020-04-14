from src.room import Room

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

# move around
current_room = hallway

while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)

