from classes.game import bcolors,Person
from classes.magic import Spell
from classes.inventory import Item
fire = Spell("fire",10,100,"black")
thunder = Spell("thunder",10,100,"black")
meteor = Spell("metor",20,200,"black")
quack = Spell("quack",14,140,"black")

cure = Spell("cure",10,100,"black")
cura = Spell("cura",10,100,"black")

potion = Item("Potiom","potion","heal 50 hp",50 )
hi_potion = Item("HI-Potiom","potion","heal 100 hp",100 )
super_potion = Item("Super-Potiom","potion","heal 500 hp",500 )
exiler = Item("exiler","exiler","full restore",9999 )
megaexiler = Item("exiler","exiler","full restore hp/mp",9999 )

player = Person(100,65,60,34,[fire,thunder,meteor,quack,cura,cure])
enemy = Person(1200, 65,20,34,[])

running = True
i=0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACK" + bcolors.ENDC)

while running:
    print("================")
    player.choose_action()
    choice = input("choose action")
    index = int(choice)-1
    if index ==0:
        dmg = player.generate_dmg()
        enemy.take_dmg(dmg)
        print("You attack for", dmg, "point of damage ", enemy.get_hp())
    elif index ==1:
        player.choose_magic()
        magic_choice =  int(input("choose magic"))-1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost> current_mp:
            print(bcolors.FAIL + "\n Not enough mp\n" + bcolors.ENDC)
            continue
        player.reduce_mp(spell.cost)
        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKGREEN + bcolors.UNDERLINE + "\n" + "heals for", str(magic_dmg))
        elif spell.type == "black":
            enemy.take_dmg(magic_dmg)
            print(bcolors.OKGREEN + bcolors.UNDERLINE + "\n" + "damage for", str(magic_dmg))
        print(bcolors.OKBLUE + "\n" + spell.name + "deals",str(magic_dmg), "point of damage" + bcolors.ENDC)
    enemy_choice = 1
    enemy_dmg = enemy.generate_dmg()
    player.take_dmg(enemy_dmg)
    print("Enemy attack for ", enemy_dmg, "player hp",player.get_hp())
    print("-----------------------------------")
    print("Enemy hp ,",bcolors.FAIL + str(enemy.get_hp()) + "/" + bcolors.ENDC)
    print("Your hp ,", bcolors.FAIL + str(player.get_hp()) + "/" + bcolors.ENDC)
    print("\n")
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you" + bcolors.ENDC)
        running = False
