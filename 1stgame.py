import os
import sys
import time
import random

hp,atk,defe,agi=10,1,2,1
clear = lambda: os.system('cls')
clear()
time.sleep(1)

def slow(a):
    for char in a:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
def raceinfo(race):
    if(race =='jelly'):hp,atk,defe,agi=10,1,2,1
    elif(race=='goblin'): hp,atk,defe,agi=11,2,2,1
    elif(race=='skeleton'): hp,atk,defe,agi=12,3,1,1
    elif(race=='wolf'): hp,atk,defe,agi=13,2,1,3
    elif(race=='tiger'): hp,atk,defe,agi=14,4,3,2
    elif(race=='theif'): hp,atk,defe,agi=15,4,1,4
    elif(race=='zombie'): hp,atk,defe,agi=20,14,4,1   
    elif(race=='human'): hp,atk,defe,agi=13,3,3,3
    elif(race=='dragon'): hp,atk,defe,agi=100,15,15,15
    else: hp,atk,defe,agi=random.randint(1,20),random.randint(1,20) ,random.randint(1,20) ,random.randint(1,20) 
        
    return (hp,atk,defe,agi)

def starname(star):
    if(star==1):   p="Weak "       
    elif(star==2): p='Normal '   
    elif(star==3): p='Elite '    
    elif(star==4): p='Rare '   
    elif(star==5): p='Boss '    
    elif(star==6): p='Epic '    
    elif(star==7): p='Legendary '    
    elif(star==8): p='Mythical '    
    else:p='??? '
    return p       
    
class monster():
     
    def monsterinfo(self, star,lv,race,name):
        self.star = star
        starname(star)
        self.lv = lv
        self.race = race
        self.name = starname(star) + name
        hp,atk,defe,agi=raceinfo(race)
        
        self.hp = hp*star*lv
        self.atk = atk*star*lv
        self.defe = defe*star*lv
        self.agi =agi*star*lv
        if(star>7):
            ex=random.randint(0,100)
            self.exp=ex*star*lv
        else:
            self.exp = star*lv
        
    def print(self):
        print('\t\t\tenemy info:\n\n')    
        print(f'\n\n\t\t\t\t\t---------------------------------------------------')
        print(f'\t\t\t\t\t|\t\tName  = {self.name:<25} |') 
        print(f'\t\t\t\t\t---------------------------------------------------')
        print(f'\t\t\t\t\t|  Race  = {self.race:<15}|   HP   = {self.hp:<13}|')
        print(f'\t\t\t\t\t|  star  = {self.star:<15}|   Atk  = {self.atk:<13}|')
        print(f'\t\t\t\t\t|  Level = {self.lv:<15}|   DEF  = {self.defe:<13}|')
        print(f'\t\t\t\t\t|  EXP   = {self.exp:<15}|   Agi  = {self.agi:<13}|')
        print(f'\t\t\t\t\t---------------------------------------------------\n\n') 
              
class player:
    def playerinfo(self, star,lv,race,name):
        
        self.star = star
        starname(star)
        self.lv = lv
        self.race = race
        self.name = name
        hp,atk,defe,agi=raceinfo(race)
        self.hp = hp*star*lv
        self.atk = atk*star*lv
        self.defe = defe*star*lv
        self.agi =agi*star*lv
        if(star>7):
            ex=random.randint(0,100)
            self.exp=ex*star*lv
        else:
            self.exp = star*lv
        
    def print(self):
        
        print(f'\n\n\t\t\t\t\t---------------------------------------------------')
        print(f'\t\t\t\t\t|\t\tName  = {self.name}                     |') 
        print(f'\t\t\t\t\t---------------------------------------------------')
        print(f'\t\t\t\t\t|  Race  = {self.race:<15}|   HP   = {self.hp:<13}|')
        print(f'\t\t\t\t\t|  star  = {self.star:<15}|   Atk  = {self.atk:<13}|')
        print(f'\t\t\t\t\t|  Level = {self.lv:<15}|   DEF  = {self.defe:<13}|')
        print(f'\t\t\t\t\t|  EXP   = {self.exp:<15}|   Agi  = {self.agi:<13}|')
        print(f'\t\t\t\t\t---------------------------------------------------\n\n')
       
def raceshow():     
    print('\t\t\t avalable race')
    print('''\t
            1.jelly      4.wolf    7.zombie
            2.goblin     5.tiger   8.human
            3.skeleton   6.theif   9.dragon\n\n''')
    
    

def lvmodecheractercreation():
    raceshow()
    ps= 1
    pl= 1
    pr=input("\t\tenter player race name : ")
    if (pr.isnumeric()==False):
        pass
    else:
        pr=int(pr)
        
    if pr==1: pr="jelly"
    elif pr==2: pr="goblin"
    elif pr==3: pr="skeleton"
    elif pr==4: pr="wolf"
    elif pr==5: pr="tiger"
    elif pr==6: pr="theif"
    elif pr==7: pr="zombie"
    elif pr==8: pr="human"
    elif pr==9: pr="dragon"
    else: pr="???"
    
    pn=input("\t\tenter player name : ")
    
    player1.playerinfo(ps,pl,pr,pn)
    time.sleep(1)
    clear()
    levelmode()    

def levelmonstercreation(gamelv):
    clear()
    if gamelv == 1:
        ms,ml,mr,mn=1,1,'jelly','slime'
    elif gamelv == 2:
        ms,ml,mr,mn=1,1,'goblin','goblin'
    elif gamelv == 3:
        ms,ml,mr,mn=1,1,'skeleton','skeleton'
    elif gamelv == 4:
        ms,ml,mr,mn=1,1,'wolf','wolf'
    elif gamelv == 5:
        ms,ml,mr,mn=1,1,'tiger','tiger'
    elif gamelv == 6:
        ms,ml,mr,mn=1,1,'zombie','zombie'
    elif gamelv == 7:
        ms,ml,mr,mn=1,1,'theif','theif'
    elif gamelv == 8:
        ms,ml,mr,mn=1,1,'human','human'
    elif gamelv == 9:
        ms,ml,mr,mn=1,1,'dragon','dragon'
    else:
        print('\nI created only 9 levels,so choose 1-9\n')
        k=input('press enter to continue: ')
        levelmap()
        
    
    
    monster1.monsterinfo(ms,ml,mr,mn)
    monster1.print()
    b = input('1. fight \n2.go back \n')
    if (b.isnumeric()==False):
                l=input("enter proper action number\n press enter to continue: ")
                levelmonstercreation(gamelv)
    else:
        b=int(b)
                
    if b == 1:
        fight1()
        
    elif b==2:
        levelmode()
    else:
        p=input('enter proper number\n press enter to continue')
        levelmonstercreation(gamelv)

def playerinfo():
    player1.print()
    b = input('go back? ')
    clear()
    levelmode()
    

player1=player()
player2=player()
monster1=monster()
player1.playerinfo(1,1,'human',"jihad")

def fight1():
    time.sleep(1)
    clear()
    healhp = monster1.hp/2
    playereng=0
    monstereng=0    
    turn = player1.name
    while player1.hp>=0 and monster1.hp>=0:
        clear()
        def windoww():
                    print(f'''\t\n\n\n
--------------------------------------------------------------------------------------------------------------------------------------------------------
        |----------------|                                                                                                 |--------------------|
        |    {player1.name:<12}|                                                                                                 | {monster1.name:^19}|
        |----------------|                                                                                                 |--------------------|
        |   HP   = {player1.hp:<6}|                                                                                                 | HP  = {monster1.hp:<13}|
        |   Eng  = {playereng:<6}|                                                                                                 | Eng = {monstereng:<13}|
        |----------------|                                                                                                 |--------------------|
--------------------------------------------------------------------------------------------------------------------------------------------------------
        
        ''')
        windoww()            
        if(turn == player1.name):
            print(f"{player1.name}'s turn")       
            action = input(f"{turn},choose an action\n1.normal\n2.special(energy needer {player1.lv} )\n3.heal\n   : ")
            if (action.isnumeric()==False):
                l=input("enter proper action number\n press enter to continue: ")
                windoww()  
                action = input(f"{turn},choose an action\n1.normal\n2.special(energy needer {player1.lv} )\n3.heal\n   : ")
            else:
                action=int(action)
            if action == 1:
                noratk= player1.atk
                monster1.hp-=noratk
                use=player1.star*2+8
                playereng+= player1.star*2+8
                print(f"{turn} just did {noratk} damage  and gain {use} energy ")
                time.sleep(2)
                clear()
                

                turn=monster1.name
            
            elif action == 2 and playereng>=player1.lv:
                spatk= player1.atk+player1.agi*2
                monster1.hp-=player1.atk+player1.agi*2
                playereng-= player1.lv
                print(f"{turn} just did special {spatk} damage using {player1.lv} energy  ")
                time.sleep(2)
                clear()
                turn=monster1.name
            
            elif action == 3 and playereng>=(player1.defe/2):
                heal = player1.defe+player1.hp/10
                player1.hp+=heal
                playereng-= player1.defe/2
                print(f"{turn} just did  {heal} heal ")
                time.sleep(2)
                clear()
                turn=monster1.name
            
            else :
                print('enter an action')
                l=input("enter proper action number\n press enter to continue: ")
                clear()
        else:  
            print(f"{monster1.name}'s turn")       
            if monster1.hp<= healhp and monstereng>=(monster1.defe/2):
                heal= monster1.defe+monster1.hp/10
                monster1.hp+=heal
                monstereng-= monster1.defe/2
                print(f"{turn} just did  {heal} heal ")
                time.sleep(2)
                clear()
                turn=player1.name
            
            elif monstereng>=monster1.lv:
                spatk= monster1.atk+monster1.agi*2
                player1.hp-=monster1.atk+monster1.agi*2
                monstereng-= monster1.lv
                print(f"{turn} just did special {spatk} damage ")
                time.sleep(2)
                clear()
                turn=player1.name
            
            else :
                noratk = monster1.atk
                player1.hp-=monster1.atk
                monstereng+= monster1.star*2+8
                print(f"{turn} just did {noratk} damage ")
                time.sleep(2)
                clear()
                turn=player1.name
                
    if player1.hp<=0:
        clear()
        windoww()
        print('''
              \n\n\n\n
---------------------------------------------------------------------------------------------------------------------------------
                                                   || MONSTER WIN ||
---------------------------------------------------------------------------------------------------------------------------------
              ''')
        time.sleep(3)
        kisukorarnai=input()
        page2()

    elif monster1.hp <=0:
        clear()
        windoww()
        print('''
              \n\n\n\n
---------------------------------------------------------------------------------------------------------------------------------
                                                   || PLAYER WIN ||
---------------------------------------------------------------------------------------------------------------------------------
              ''')
        time.sleep(3)
        kisukorarnai=input()
        page2()

    else:
        clear()
        windoww()
        print('''
              \n\n\n\n
---------------------------------------------------------------------------------------------------------------------------------
                                                   || DRAW ||
---------------------------------------------------------------------------------------------------------------------------------
              ''')
        time.sleep(3)
        kisukorarnai=input()
        page2()
            

        
def page1():
    print('''\t\t\t\t\t\t\t==================================''')
    print('''\t\t\t\t\t\t\t|| Welcome to the unknown world ||''')
    print('''\t\t\t\t\t\t\t==================================\n\n\n\n\n\n\n\n''')
    time.sleep(1)
    a="Press enter key to continue............ "
    slow(a)
    b=input()
    clear()
    print('\n\n\n\n\n\n')
    a="............................................................LOADING............................................................ "
    slow(a)
    
    time.sleep(1)

def page2():
    clear()
    print('''\t\t\t\t\t\t\t|-----------------------------|''')
    firstmess= '\t\t\t\t\t\t\t|choose mode:                 |'
    slow(firstmess)
    print('''\n\t\t\t\t\t\t\t|\t1.story mode          |''')
    print('''\t\t\t\t\t\t\t|\t2.Level mode          |''')
    print('''\t\t\t\t\t\t\t|\t3.PVE custom mode     |''')
    print('''\t\t\t\t\t\t\t|\t4.PVP mode            |''')
    print('''\t\t\t\t\t\t\t|\t5.PVP custom mode     |''')
    print('''\t\t\t\t\t\t\t|-----------------------------|''')
    print('\n\n\n')
    playmode=input("                   enter play mode: ")
    clear()
    modechoise=page2_1(playmode)
    time.sleep(1)
    
    return modechoise
def page2_1(playmode):
    if (playmode == '1' or playmode == "story mode" or playmode == "story" or playmode == "Story mode" or playmode == "Story"):
        a="You have choosen Story mode"
        slow(a)
        time.sleep(1)
        storymode()
        return 1
    elif(playmode == '2' or playmode == "Level mode" or playmode == "Level" or playmode == "level mode" or playmode == "level"):
        a="You have choosen Level mode"
        slow(a)
        time.sleep(1)
        levelmode()
        
        return 2
    elif(playmode == '3' or playmode == "PVE custom mode" or playmode == "PVE" or playmode == "pve custom mode" or playmode == "pve"):
        a="You have choosen PVE custom mode"
        slow(a)
        time.sleep(1)
        pvemode()
        
        return 3
    elif(playmode == '4' or playmode == "PVP mode" or playmode == "PVP" or playmode == "pvp mode" or playmode == "pvp"):
        a="You have choosen PVP mode"
        slow(a)
        time.sleep(1)
        pvpmode()
        
        return 4
    elif(playmode == '5' or playmode == "PVP custom mode" or playmode == "pvp custom mode"):
        a="You have choosen pvp custom mode"
        slow(a)
        time.sleep(1)
        pvpcustommode()
        
        return 5
    else:
        print('choose a proper mode')
        time.sleep(1)
        page2()
        
def levelmode():
    print('\n\n\n')
    print('''\t\t\t\t1. create player cheracter''')
    print('''\t\t\t\t2. Level map''')
    print('''\t\t\t\t3. player info''')
    print('\n\n')
    choise = input('\t\tenter a number: ')
    time.sleep(1)
    clear()
    if choise == "1":
        lvmodecheractercreation()
        
    elif choise == '2':
        levelmap()
        
    elif choise == '3':
        playerinfo()
        
    else:
        print('enter proper number')
        k=input('press enter to continue: ')
        levelmode()
              
def levelmap():
    clear()
    print('''
         |---------------------------------------------------------------------------------|
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |   1 | |   2 | |   3 | |   4 | |   5 | |   6 | |   7 | |   8 | |   9 | |  10 | | 
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |  11 | |  12 | |  13 | |  14 | |  15 | |  16 | |  17 | |  18 | |  19 | |  20 | | 
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |  21 | |  22 | |  23 | |  24 | |  25 | |  26 | |  27 | |  28 | |  29 | |  30 | | 
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |  31 | |  32 | |  33 | |  34 | |  35 | |  36 | |  37 | |  38 | |  39 | |  40 | | 
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |  41 | |  42 | |  43 | |  44 | |  45 | |  46 | |  47 | |  48 | |  49 | |  50 | | 
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |  51 | |  52 | |  53 | |  54 | |  55 | |  56 | |  57 | |  58 | |  59 | |  60 | | 
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |  61 | |  62 | |  63 | |  64 | |  65 | |  66 | |  67 | |  68 | |  69 | |  70 | | 
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |  71 | |  72 | |  73 | |  74 | |  75 | |  76 | |  77 | |  78 | |  79 | |  80 | | 
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |  81 | |  82 | |  83 | |  84 | |  85 | |  86 | |  87 | |  88 | |  89 | |  90 | | 
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | |  91 | |  92 | |  93 | |  94 | |  95 | |  96 | |  97 | |  98 | |  99 | | 100 | | 
         | |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |-----| |
         | ------------------------------------------------------------------------------- |
          ''')
    gamelv = input("enter level: ")
    if (gamelv.isnumeric()==False):
        l=input("enter proper level number\n press enter to continue: ")
        levelmap()
    else:
        gamelv=int(gamelv)
    	
    time.sleep(1)
    clear()
    levelmonstercreation(gamelv)
       
def storymode():
    print('\nonly level mode available')
    p=input("press enter to back: ")
    page2()
    
def pvemode():
    print('\nonly level mode available')
    p=input("press enter to back: ")
    page2()
def pvpmode():
    print('\nonly level mode available')
    p=input("press enter to back: ")
    page2()
def pvpcustommode():
    print('\nonly level mode available')
    p=input("press enter to back: ")
    page2()

   
page1()  
page2()   
 



