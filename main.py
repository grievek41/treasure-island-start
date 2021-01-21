# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 

# #https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


# L = "left"
# R = "right"
# S = "swim"
# W = "wait"
# Y = "yellow"
# B = "blue"
# R = "red"
# # can use .lower() to turn answers to all lowercase.

# choice1 = input("Do you want to go left or right L or R?\n ")
# if choice1 == "L":
#   print(f' Great job! You have gone {L} and found a trail leading to a lake! ')
#   choice_2 = input("Should you swim or wait S or W?\n ") 
#   if choice_2 == "S":
#     print(f"Great job! by chossing to {S}, we did not drown in a leaky boat! ")
#     choice_3 = input("You see three doors, one yellow, one blue, and one red which do you choose? Y or B or R?\n ")
#     if choice_3 == "Y":
#       print("You have chosen the {Y} door, You have found the treasure! CONGRATULATIONS!")
#     else:
#       print("You have chosen the wrong door! GAME OVER!")
#   else: 
#     print(f"By choosing {W}, we have waited for a boat which has sprung a leak and you drown! GAME OVER!")
# else: 
#   print(f'Oh no! You have gone {R}, and fallen down



print('''
            _.-':_.-'                      '-._   ~     ~
                  _.-'                                   '-._.'-._
   ~       .-'.-,'                                                '-.
           '-._                       /\   /\                    _.-'
 ~             '-.           (o)(o)  /  \ /  \                ._'
           ~      '-._         (/      /\ (           _.'-._,-'
                      '-._            /  \ )      _.-'   (o o)
 ~     ) ( ) (    ~     .-'               (     .'       ))~((  ~
      ) " ( " (        .-'                 )    '-._.,.            ~
     )  "  ("  (       '-._               /           '-._  ~ 
    )   "   (   ( ___      '-._          (                '.   ~
        "   "    |   | ~      .'          )                '-._
  ---._-|--|--|--|--/     _.-'           /  (o)(o)           _.'   ~
       \ o  o  o  o/     '-._           /    (  )           '-._-'-.
   ~~~~~~~~~~~~~~~~~         '-._      (                        _.-'
  ~          ~             ~     '-.    ) /\            _.-"._,'
                  ~              _.'   / /\ /\         '.  ~    (o o)
    (o o)              _.-'-._.-'     / /  \  \          '-._._ ))~((
    ))~(( ~        _.-'              /                         '-. ~
                .-'              .-'('-._                        '-.
 ~            _.'         _.-'-.-'~   ~  '.             _.'-.-'._  .'
     .-'=_.'-'         .-'  ~   ~   _ _.-'          _.-'     ~   '.'
  _.-'                 '-._,.-'._.-'    (o)(o)     '_   ~       ~
.'                                         \)         '-._   ~    ~
'-.- = .-'.     (o)(o)                                    '=._
          '._    (  )                                         '-.
LGB     ~    :_                                            _.-'.-' ~
     ~     ~   "._,-'.-'._    .-`-._;'-._.='._          .-'  ~
                    ~     '-_."      ~    ~   '-._:'=~_.'       ~
           ~     ~      ~        ~     ~        ~          ~    ~
           ''')

           
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("Be careful, adventurer, this island is full of hidden pitfalls and dangers!")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


N = "north"
E = "east"
S = "south"
W = "west"

D = "doggy paddle"
C = "canoe"
P = "pole-vault"
R = "right"
L = "left"
P1 = "path one"
P2 = "path two"
P3 = "path three"
P4 = "path four"
T1 = "trail one"
T2 = "trail two"
T3 = "trail three"

Y = "yes"
N = "no"
# can use .lower() to turn answers to all lowercase.

choice_1 = input('Which direction shall we go ? We can go "N" for north, "E" for east, "W" for west, and "S" for south.\n')

if choice_1 == "N":
  print(f'You have gone 50 paces {N} and found a hidden trail leading to a beautiful stream and waterfall, behind that waterfall.... ')
  
  if choice_1 == "E":
    print(f"You have gone 50 paces {E} and have encountered man-eating cannibals. GAME OVER!")
    
    if choice_1 == "W":
      print(f"You have gone 50 paces {W} and have stumbled across angry pirates, who make you walk the plank. GAME OVER!")

  choice_2 = input('Do you see the cave behind the waterfall adventurer ? Should you swim "D", canoe "C", or polevault "P"?.\n ')       
  
  if choice_2 == "D":
    print(f"You have chosen to {D}, a school of hungry piranha have found you. GAME OVER! ")
    
  if choice_2 == "P":
    print(f'You have chosen to {P}, you have pole-vaulted right into the cave!\n ')

    choice_3 = input('Shortly after entering the cave you come to a fork. Which way do you go? "R" for right, "L" for left \n')
    
    if choice_3 == "L":
      print(f'You have chosen {L}, following the path you come to a small vine filled opening..\n')
    
      choice_4 = input('Tearing your way through the vines you find that you are not only in a large graveyard,\n but you are not alone. There are four paths that lead into the darkness.\n Hurry choose a path! "P1", "P2", P3", or "P4".\n')
    
      if choice_4 == "P1":
        print(f"You chose {P1}, and are immediately overrun with brain-eating zombies. GAME OVER!")

      if choice_4 == "P2":
        print(f"You chose {P2}, halfway down the path you step into a large mud hole and are pulled under by scaly hands. GAME OVER!")
      
      if choice_4 == "P3":
        print(f"You chose {P3}, you reach the end of the terrifying graveyard and climb over the gate....\n")
      
        choice_5 = input('Topping the rise you see a foreboding castle in the distance, and three different trails to get there, one goes down the hill across the open beach,\n the next goes through a dark forest, the last  goes up a rugged mountain.\n "T1", "T2" for the dark forest trail, and "T3" for the trail up the rugged mountain.\n')
        
        if choice_5 == "T1":
          print(f"You chose {T1}, you run across the beach and up to the castle.")
          if choice_5 == "T2":
            print(f'You chose {T2}, upon entering the dark forest you are quickly swallowed whole by a cyclops. GAME OVER!')
         
          choice_6 = input('Do you open the door ? "Y" for yes, "N" for no.\n')
          
          if choice_6 == "Y":
            print(f'You chose {Y}, and are now standing in a large room filled with gold and jewels. CONGRATULATIONS!!! You have won the game!')
          
          else:
            print('What a loser!!, to come so close and yet mess it up!')
          
        else:
         print(f'You chose {T3}, on your way up the mountain a billy goat mistakes you for a trampoline. GAME OVER!')
  
      else:
        print(f'You chose {P4}, while tying your shoes you are bitten by a bat and have to remain in the graveyard forever. GAME OVER!')
    
    else:
      print(f'You have chosen {R}, some way up the fork you accidentally step on the tail of a sleeping bear. GAME OVER! ')
      
  else:
    print(f'You have chosen {C}, too bad it was filled with holes, here come the piranha. GAME OVER! ')
else:
  print(f'You have gone 50 paces {S} and have come to the edge of a high cliff, and lose your footing. GAME OVER!')