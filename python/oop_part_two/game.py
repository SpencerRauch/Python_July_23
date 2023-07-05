from game_classes.fighter import Fighter
from game_classes.viking import Viking
from game_classes.ninja import Ninja
import random

generic = Fighter()

# generic.use_special()

leif = Viking("Leif")
chuck = Ninja("Chuck")

while leif.health > 0 and chuck.health > 0:
    print("Welcome to Chuck vs Leif, you're Chuck!")
    response = ""
    while response != '1' and response != '2' and response != '3':
        response = input("Choose an action \n 1) Attack \n 2)Use Special \n 3)Use Buff \n>>>")
    if response == '1':
        chuck.attack(leif)
    elif response == '2':
        chuck.use_special(leif)
    else:
        chuck.use_buff(leif)
    leifs_move = random.randint(1,3)
    if leifs_move == 1:
        leif.attack(chuck)
    elif leifs_move == 2:
        leif.use_special(chuck)
    else:
        leif.use_buff(chuck)

if chuck.health > 0:
    print("You win!")
elif leif <= 0:
    print("Tie")
else:
    print("How could this happen? Chuck Norris lost")
