import random

class player:
    hp = 0
    defence = 0

    def __init__(self, hp, defence):
        self.hp = hp
        self.defence = defence

    def Kick(self):
        self.damage = random.randint(1, 3)
        return self.damage

class enemy:
    hp = 0
    defence = 0

    def __init__(self, hp, defence):
        self.hp = hp
        self.defence = defence

    def Kick(self):
        self.damage = random.randint(1, 3)
        return self.damage

random.seed()

player1 = player(6, 1)
player2 = enemy(10, 0)
turn = 1

while (player1.hp>0 and player2.hp>0):
    if (turn == 1):
        damage = player1.Kick()
        if (damage - player2.defence >= 1):
            player2.hp -= (damage - player2.defence)
            print("Player 1 do a Kick!")
            print("Player 2 HP is now " + str(player2.hp))
        else:
            print("Player 1 do a Kick!")
            print("But Player 2 has blocked attack!")
    if (turn == -1):
        damage = player2.Kick()
        if (damage - player1.defence > 1):
            player1.hp -= (damage - player1.defence)
            print("Player 2 do a Kick!")
            print("Player 1 HP is now " + str(player1.hp))
        else:
            print("Player 2 do a Kick!")
            print("But Player 1 has blocked attack!")

    print("")
    turn *= -1

if (player1.hp<=0):
    print("Player 2 is winner!")
elif (player2.hp<=0):
    print("Player 1 is winner!")