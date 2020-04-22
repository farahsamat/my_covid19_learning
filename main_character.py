from src.character import Character, Enemy

dave = Enemy("Dave", "A smelly zombie") #Enemy is a Character
pea_shooter = Character("Pea Shooter", "A plant that will shoot peas any zombie in sight")

dave.set_conversation("Brainnnnnnn")
dave.talk()

pea_shooter.set_conversation("Pew Pew Pew")
pea_shooter.talk()