from chatacter import Character, Asssin, Vompire, Ninja, Samurai

player_1 = Ninja(name='Vasya', hp=1000, damage=2)
print(player_1.stats())
player_2 = Samurai(name='Petya', hp=20, damage=3)
print(player_2.stats())

for i in range(3):
    player_2.deal_who(player_1)
    player_1.deal_who(player_2)

    print(player_1.stats())
    print(player_2.stats())