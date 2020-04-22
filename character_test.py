from src.character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.set_weakness("cheese")

dave.get_weakness()

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)
