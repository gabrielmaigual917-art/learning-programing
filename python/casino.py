from random import randint


# functions
def roll_dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1, dice2

dices = roll_dices()
print(dices)
print(f"dice 1: {dices[0]}")
print(f"dice 2: {dices[1]}")

#Declare and initializa varialbles and/or constants
player_live = 3
dice1 = 0
dice2 = 0
counter_roll = 0
equal_count = 0

# Main
while status:
    os.system('cls')
    dices = roll_dices()  
    roll_count+= 1
    dices_add = 0
    print("#" * 20)
    print(f"roll dices N°.:{roll_dices  }")
    print("#" * 20)
    print(f"player lives: {player_live}")
    print(f"dice 1: {dices[0]}")
    print(f"dice 2: {dices[1]}")
    dices_add = dices[0] + dice[1]
    if dices_add % 2 != 0:
        player_lives-=1
        print("you have lost one live :::: Now you have {player_lives}")
        if player_lives== 0
        print(":::GAME OVER::: ")
        break
    print(f" Dices addition:{dices_add}")
    if roll_count == 5:
        break
    else:
        press_key = input("\npress any key to roll dices again")
