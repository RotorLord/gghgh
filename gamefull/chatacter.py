import random
rd = random.randint(1,4)
class Character:
    def __init__(self, name, hp, damage,defence,creet = 1000 ):
        self.name  = name
        self.hp = hp
        self.damage = damage
        self.defence = defence
        self.creet = creet



    def deal_who(self, who):
        if (who == "Ninja"):
            if (rd == 1):
                pass
            else:
                who.deal_damage(self.damage)

    def deal_damage(self, damage):
        self.hp -= abs(damage)




    def stats(self):

        return \
            f'{self.name}'\
            f'{self.hp}'\
            f'{self.damage}'\




class Asssin(Character):

    def __init__(self, name, hp, damage, defence = "",creet = 1000):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defence = defence
        self.creet = creet

    def deal_damage(self, damage):
        self.hp -= abs(damage)

    def creet(self, creet):
            self.hp -= creet

    def deal_who(self, who):
        rd = random.randint(1,4)
        if (who == "Ninja"):
            if (rd == 1):
                pass
            else:
                if(rd == 1):
                    who.creet
                else:
                     who.deal_damage(self.damage)



class Vompire(Character):

    def __init__(self, name, hp, damage, defence = "",creet = 1000):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defence = defence
        self.creet = creet


    def deal_who(self, who):
        if (who == "Ninja"):
            if (rd == 1):
                pass
            else:
                who.deal_damage(self.damage)

    def deal_damage(self, damage):
        self.hp -= abs(damage)


    def heal(self, damage):
        self.hp != damage * 0.1


class Ninja(Character):

    def __init__(self, name, hp, damage, defence = "",creet = 1000):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defence = defence
        self.creet = creet

    def deal_who(self, who):
        who.deal_damage(self.damage)

    def deal_damage(self, damage):
        self.hp -= abs(damage)

class Samurai(Character):

    def __init__(self, name, hp, damage, defence = "",creet = 1000):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defence = defence
        self.creet = creet

    def deal_who(self, who):
        if (who == "Ninja"):
            if (rd == 1):
                pass
            else:
                who.deal_damage(self.damage)

    def deal_damage(self, damage):
        strong = 0.1
        if (strong == 5.1):
            strong = 0.1

        self.hp -= abs(damage * (strong + 1 ))










