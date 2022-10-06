from enum import  Enum, auto
from item import Item, weapone
from chatacter import Character
class CharacterStats(Enum):
    HP = auto()
    DAMAGE = auto()
    ARMOR = auto()


class Character_item(Character):
    def __init__(self, name = "", hp = 30, damage = 1, armour = 1):
        Character.__init__(self, name , hp, damage,armour)
        self.weapon = None
        self.armor = None


    def set_armor(self, item: Item):
        self.armor = item

    def set_weapon(self, item: Item):
        self.weapon = item

    def attack(self, target):
        try:
            add_damage = self.weapon.use[CharacterStats.DAMAGE]
        except Exception as er:
            print(f'что то не так {er}')
            add_damage = 0
            target.deal_damage(self.damage + add_damage)

    def take_damage(self, player):
        try:
           minus_damage = self.armor.use[CharacterStats.ARMOR]
           if self.damage == self.defence:
               damgTaken = 0
           else:
               damgTaken = self.damage - self.defence

        except Exception as er:
            print(f'что то не так {er}')
            minus_damage = 0












