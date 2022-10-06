
from item import Item
from characterSPESIAL import CharacterStats as stat, Character_item

player1 = Character_item(name = "smt")
player2 = Character_item(name = "tms")

sword1 = Item("Ложка", stat ={stat.DAMAGE: 3}, durabillity = 10)
sword2 = Item("Ручка", stat ={stat.DAMAGE: 1}, durabillity = 10)

player1.set_weapon(sword1)
player2.set_weapon(sword2)

while player1.hp > 0 and player2.hp > 0:
    player1.attack(player2)
    player2.attack(player1)
    print(player1.hp)
    print(player2.hp)
