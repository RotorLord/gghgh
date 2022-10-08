import random

class Die (Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

class start_Depretion(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

class OwePayBunk(Exception):
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return  self.text

class Action():
    def __init__(self, name, hp, happy, money):
        self.name = name
        self.hp = hp
        self.happy = happy
        self.money = money

class Work(Action):
    def __init__(self, name, hp, happy, money):
        super().__init__(name, hp, happy, money)
        self.name = name
        self.hp = hp
        self.happy = happy
        self.money = money

class rest(Action):
    def __init__(self, name, hp, happy, money):
        super().__init__(name, hp, happy, money)
        self.name = name
        self.hp = hp
        self.happy = happy
        self.money = money

class pearson():

    try:

        while True:
            def __init__(self, name = None, hp = 1, happy=  1 ,money = 1):
                self.name = name
                self.hp = hp
                self.happy = happy
                self.money = money


            def set_status(self,money,happy):
                self.hp = random.randint(-1,10)
                if self.hp < 0:
                    raise Die("У вас кончилась желание жить")
                self.happy = random.randint(-10, 10)
                if self.happy < 0:
                    raise start_Depretion("У вас депрессия")
                self.money = random.randint(-50,100)
                if self.money < 0:
                    raise OwePayBunk("Вы должны деньги банку")

            def do(self, action: Action):
                baffhp = 1
                baff = 1
                if type(action == Work):
                    if self.happy > 90:
                        baff = 1.1
                elif type(action == rest):
                    if self.hp < 40:
                        baffhp = 0.8
                self.set_status(happy = self.happy * baffhp, money= self.money * baff)

            def __str__(self):
                return \
                f'{self.name}' \
                f'{self.hp}' \
                f'{self.happy}' \
                f'{self.money}'\

    except Die:
        print("you die")
    except start_Depretion:
        print("start depreion")
    except OwePayBunk:
        print("you must pay")






