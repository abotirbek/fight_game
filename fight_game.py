import random
class Player:
    def __init__(self,name,heart,power,aid,magic):
        self.name = name
        self.hp = heart
        self.power = power
        self.aid = aid
        self.magic = magic
        self.aid_count = 3
        self.magic_count = 1
    def __sub__(self, other):
        self.hp -= other.power
        return f"{self.name.capitalize()}: HP={self.hp}, Power={self.power}"
    def __add__(self, other):
        if self.aid_count > 0:
            self.hp += other.aid
            self.aid_count -= 1
        return f"\n --- {self.name.capitalize()} used AIDS! --- \n{self.name.capitalize()}: HP={self.hp}, Power={self.power}\n"
    def __mul__(self, other):
        if self.magic_count > 0:
            self.hp *= other.magic
            self.magic_count -= 1
        return f"\n --- {self.name.capitalize()} used MAGIC! --- \n{self.name.capitalize()}: HP={self.hp}, Power={self.power}\n"
    def __abs__(self):
        return f"\n --- Game Over --- \n{self.name.capitalize()}'s lost"

class Enemy(Player):
    def __init__(self,name,heart,power,aid,magic):
        Player.__init__(self,name,heart,power,aid,magic)

nickname = input("Enter nickname: ")
heart_random = random.randint(100,200)
power_random = random.randint(10,50)
pl = Player(nickname,100,30,25,2)
en = Enemy('Night',heart_random,power_random,25,2)
while True:
    if pl.hp <= 0:
        print(abs(pl))
        break
    if en.hp <= 0:
        print(abs(en))
        break
    answer = input("\nFire, Aid, Magic: ")
    if answer.lower() == 'f':
        print(en - pl)
        print(pl - en)
    elif answer.lower() == 'a':
        print(pl+pl)
    elif answer.lower() == 'm':
        print(pl*pl)
