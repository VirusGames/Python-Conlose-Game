import random
import math
import os

turn = 1
clear = lambda: os.system('cls')

class Game:
    print("               Welcome to the game!               ")
    print("           print numbers to select option         ")
    print("      add \"i\" to get information about option   ")
    print("         print \"q\" to exit from option          \n")

    effect_list = [["scene.player1.MP+=min(scene.player1.maxMP-scene.player1.MP,10)",10],
                   ["scene.player2.MP+=min(scene.player2.maxMP-scene.player2.MP,10)",20]]

    def __init__(self):
        self.player1 = player(100, 100, 0, 0, 1)
        self.player2 = enemy()

    def Menu(self):
        funclist = ["Attack", "Defense", "Spell", "Items", "Info", "Skip_Turn"]
        infolist = ["Contains free low-damage attacks.",
                    "Increase your defense for 1 turn.",
                    "Contains high-damage or applying effects attacks that consumes MP.",
                    "Show item you have and can use.",
                    "Show information about player and enemy.",
                    "You just do nothing and skip the turn."]
        print("1.ATTACK"+" "*15+"2.DEFENSE")
        print("3.SPELL"+" "*16+"4.ITEMS")
        print("5.INFO"+" "*17+"6.SKIP TURN")
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
            self.player2.HP -= int(max(damage - self.player2.defence, 1))

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
                self.player2.HP -= int(max(damage - self.player2.defence, 1))
            else:
                print("Not enough MP for this spell\n")
                self.Spell()

    def Items(self):
        print("Work in progress!\n")
        self.Menu()

    def Info(self):
        print(self.player1.name + " " * 18 + self.player2.name)
        print("HP " + str(self.player1.HP) + "/" + str(self.player1.maxHP) + " " * (16 - len(str(
            self.player1.HP))) + "HP " + str(self.player2.HP) + "/" + str(self.player2.maxHP))
        print("MP " + str(self.player1.MP) + "/" + str(self.player1.maxMP) + " " * (16 - len(str(
            self.player1.MP))) + "MP " + str(self.player2.MP) + "/" + str(self.player2.maxMP))
        print("Def " + str(self.player1.defence) + " " * (19 - len(str(
            self.player1.defence)))  + "Def " + str(self.player2.defence) + "\n")
        self.Menu()

    def Skip_Turn(self):
        pass


class player:
    name = "Reimu"
    attack_list = [["Persuasion Needle", "Needle"], ["Dimensional Rift", "Rift"]]
    attack_infolist = \
    ["These needles is the best choice for exterminating youkais!\nDeals 10-30 damage",
     "Instantly teleport and strike at the enemy!\ndeals 20 damage"]
    spell_list = [["Spirit Sign ~ \"Fantasy Seal\"", "Fantasy_Seal", 10]]
    spell_infolist = \
        ["Overwhelms the enemy with a huge flood of homing shots!\nDeals 5 damage per 10 MP\nconsumes all MP"]

    def __init__(self, hp, mp, defence, damage, ID):
        self.HP = hp
        self.maxHP = hp
        self.MP = mp
        self.maxMP = mp
        self.defence = defence
        self.defence = defence
        self.ID = ID

    def Needle(self):
        print(self.name+" uses Persuasion Needle!")
        damage = random.randint(10, 30)
        print("And deals "+str(damage)+"!\n")
        return damage

    def Rift(self):
        print(self.name + " uses Dimensional Rift!")
        damage = 20
        print("And deals " + str(damage) + "!\n")
        return damage

    def Fantasy_Seal(self):
        print(self.name+' uses Spirit Sign ~ "Fantasy Seal"!')
        damage = int((self.MP-self.MP%10)/10*5)
        self.MP -= int(self.MP-self.MP%10)
        print("And deals " + str(damage) + "!\n")
        return damage

    def Defence(self):
        print(self.name+" is Defensing!\nHer defence has increased by 1 by 1 turn\n")
        self.defence += 1
        temp_turn = turn
        string = "temp_turn=" + str(
            temp_turn) + ";\nif(turn == temp_turn+1):scene.player1.defence-=1;DeleteList(scene.effect_list," + str(
            10 * self.ID + 1) + ");print(scene.player1.name+'\\'s Defence was broken.')"
        Game.effect_list.append([string, 10*self.ID+1])


class enemy:
    name = "Blue Fairy"

    def __init__(self):
        self.HP = 80
        self.maxHP = 80
        self.MP = 50
        self.maxMP = 50
        self.defence = 0
        self.damage = 2
        self.ID = 2

    def Danmaku(self):
        print(self.name + " uses Circle Danmaku!")
        damage = random.randint(10, 25)+self.damage
        print("And deals " + str(damage) + "!\n")
        return damage

    def Familiar(self):
        print(self.name + " uses Familiar trio!\n")
        self.damage += 9
        self.MP -= 30
        temp_turn = turn
        string = "temp_turn=" + str(
            temp_turn) + ";\nif(turn == temp_turn+2):scene.player2.damage-=9;DeleteList(scene.effect_list," + str(
            10 * self.ID + 2) + ");print('Familiars were disappeared.')"
        Game.effect_list.append([string, 10 * self.ID + 2])

    def Defence(self):
        print(self.name+" is Defensing!\nHer defence has increased by 1 by 1 turn\n")
        self.defence += 1
        temp_turn = turn
        string = "temp_turn=" + str(
            temp_turn) + ";\nif(turn == temp_turn+1):scene.player2.defence-=1;DeleteList(scene.effect_list," + str(
            10 * self.ID + 1) + ");print(scene.player2.name+'\\'s Defence was broken.')"
        Game.effect_list.append([string, 10*self.ID+1])


def DeleteList(list, value):
    num = 0
    for i in range(len(list)):
        #print(i - num)
        if (list[i - num][1] == value):
            list.pop(i - num)
            num += 1
    return list

def FindLists(list, command):
    num = 0
    Donelist = []
    for i in range(len(list)):
        if(eval(command)):
            Donelist.append(i)
    return Donelist

def first_n_digits(num, n):
    return num // 10 ** (int(math.log(num, 10)) - n + 1)

def UseList(scene, nums):
    num = 0
    exception(num)

def exception(num):
    nums = FindLists(scene.effect_list, "first_n_digits(list[i][1],1)==1")
    for i in nums:
        try:
            exec(scene.effect_list[i][0])
        except IndexError:
            num += 1
            exception(num)

scene = Game()

while (scene.player1.HP>0 and scene.player2.HP>0):
    nums = FindLists(scene.effect_list, "first_n_digits(list[i][1],1)==1")
    UseList(scene, nums)
    scene.Menu()

    nums = FindLists(scene.effect_list, "first_n_digits(list[i][1],1)==2")
    UseList(scene, nums)
    while True:
        rand = random.random()
        if (rand<1/3):
            damage = scene.player2.Danmaku()
            scene.player1.HP -= int(max(damage - scene.player1.defence, 1))
            break
        elif (rand>=1/3 and rand<2/3 and scene.player2.MP >= 30):
            scene.player2.Familiar()
            break
        elif (rand>=2/3):
            scene.player2.Defence()
            break

    turn += 1

if (scene.player1.HP<=0):
    print("You lose!\nGood luck for the next time!")
elif (scene.player2.HP<=0):
    print("Congratulations! You win!")
