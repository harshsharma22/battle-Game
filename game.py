import random
from .magic import Spell
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD ='\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


class Person:
    def __init__(self,hp,mp,attk,defence,magic):
        self.maxhp=hp
        self.hp=hp
        self.maxmp=mp
        self.mp=mp
        self.attkl = attk-10
        self.attkh=attk+10
        self.df=defence
        self.magic=magic
        self.actions = ['Attack','Magic']

    def generate_dmg(self):
        return random.randrange(self.attkl, self.attkh)


    def take_dmg(self,dmg):
        self.hp -= dmg
        if self.hp<0:
            self.hp = 0
        return self.hp
    def heal(self,dmg):
        self.hp+= dmg
        if self.hp >self.maxhp:
            self.hp =self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self,cost):
        self.mp -=cost

    def choose_action(self):
        print("action")
        i=1
        for item in self.actions:
            print(str(i) + "i", item)
            i+=1
    def choose_magic(self):
        print("magic")
        i=1
        for spell in self.magic:
            print(str(i) + "", spell.name, "(cost:",str(spell.cost) + ")")
            i=i+1
