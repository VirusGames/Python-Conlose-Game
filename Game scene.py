import random
import colorama
import math

turn = 1

class Game:
    print("               Welcome to the game!               ")
    print("            Now there just player input           ")
    print("           print numbers to select option         ")
    print("      add \"i\" to get information about option   ")
    print("         print \"q\" to exit from option          \n")

    effect_list = []

    def __init__(self):
        self.player1 = player(100, 100, 0, 1)
        self.player2 = enemy(80, 50, 0, 2)

    def Menu(self):
        funclist = ["Attack", "Defense", "Spell", "Skip_Turn"]
        infolist = ["Contains free low-damage attacks",
                    "Increase your defense for 1 turn",
                    "Contains high-damage or applying effects attacks that consumes MP",
                    "You just do nothing and skip the turn"]
        print("1.ATTACK        2.DEFENSE")
        print("3.SPELL         4.SKIP TURN")
        num = input().lower()
        if ("i" in num):
            print(infolist[int(num[0])-1]+"\n")
            self.Menu()
        else:
            print("")
            eval("self."+funclist[int(num[0])-1]+"()")

    def Attack(self):
        list = self.player1.attack_list
        for i in range(len(list)):
            print(str(i+1)+"."+list[i][0])
        num = input().lower()
        if ("i" in num):
            print(self.player1.attack_infolist[int(num[0])-1]+"\n")
            self.Attack()
        elif ("q" in num):
            print("")
            self.Menu()
        else:
            damage = eval("self.player1."+list[int(num[0])-1][1]+"()")
            self.player2.HP -= damage

    def Defense(self):
        self.player1.Defence()

    def Spell(self):
        list = self.player1.spell_list
        for i in range(len(list)):
            print(str(i+1)+"."+list[i][0])
        num = input().lower()
        if ("i" in num):
            print(self.player1.spell_infolist[int(num[0])-1]+"\n")
            self.Spell()
        elif ("q" in num):
            print("")
            self.Menu()
        else:
            if(self.player1.MP>=list[int(num[0])-1][2]):
                damage = eval("self.player1."+list[int(num[0])-1][1]+"()")
                self.player2.HP -= damage
            else:
                print("Not enough MP for this spell\n")
                self.Spell()
    def Skip_Turn(self):
        pass

class player:
    name = "Reimu"
    attack_list = [["Persuasion Needle", "Needle"], ["Dimensional Rift", "Rift"]]
    attack_infolist = \
    ["These needles is the best choice for exterminating youkais!\nDeals 10-30 damage",
     "Instantly teleport and strike at the enemy!\ndeals 20 damage"]
    spell_list = [["Spirit Sign ~ \"Fantasy Seal\"", "Fantasy_Seal", 60]]
    spell_infolist = \
        ["Overwhelms the enemy with a huge flood of homing shots!\nDeals 60 damage\nconsumes 60 MP"]

    def __init__(self, hp, mp, defence, ID):
        self.HP = hp
        self.maxHP = hp
        self.MP = mp
        self.maxMP = mp
        self.defence = defence
        self.ID = ID

    def Needle(self):
        print(self.name+" uses Persuasion Needle!")
        self.damage = random.randint(10, 30)
        return self.damage

    def Rift(self):
        print(self.name + " uses Dimensional Rift!")
        self.damage = 20
        return self.damage

    def Fantasy_Seal(self):
        print(self.name+' uses Spirit Sign ~ "Fantasy Seal"!')
        self.damage = 60
        self.MP -= 60
        return self.damage

    def Defence(self):
        print(self.name+" is Defensing!\nHer defence has increased by 1 by 1 turn")
        self.defence += 1
        temp_turn = turn
        string = "temp_turn="+str(temp_turn)+";\nif(turn == temp_turn+1):self.player1.defence-=1;DeleteList(Game.effect_list,"+str(10*self.ID+1)+");print('Defence was broken')"
        Game.effect_list.append([string, 10*self.ID+1])


class enemy:
    name = "Blue Fairy"

    def __init__(self, hp, mp, defence, ID):
        self.HP = hp
        self.maxHP = hp
        self.MP = mp
        self.maxMP = mp
        self.defence = defence
        self.ID = ID

    def Danmaku(self):
        print(self.name + " uses Circle Danmaku!")
        self.damage = random.randint(1, 3)
        return self.damage

def DeleteList(list, value):
    num = 0
    for i in range(len(list)):
        #print(i - num)
        if (list[i - num][1] == value):
            list.pop(i - num)
            num += 1
    return list

def FindList(list, command):
    num = 0
    Donelist = []
    for i in range(len(list)):
        if(eval(command)):
            Donelist.append(i)
    return Donelist

def first_n_digits(num, n):
    return num // 10 ** (int(math.log(num, 10)) - n + 1)

scene = Game()

scene.Menu()

#list = [["oooo", 11], ["aaaa", 12], ["aaaa", 23]]
#i = FindList(list, "first_n_digits(list[i][1],1)==1")
#print(i)

"""list = [["oooo", 11], ["aaaa", 12]]
num = 0
for i in range(len(list)):
    print(i-num)
    if(list[i-num][1]==11):
        list.pop(i-num)
        num+=1
print(list)"""