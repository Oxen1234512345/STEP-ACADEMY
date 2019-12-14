import random
again = 'Yes'
while again == 'Yes':
    user_choice = 0
    user_score = 0
    door_count = int(input('Input door (more or equal 3): '))
    if door_count < 3:
        print('Error. Number of doors must be more or equal 3')
        door_count = int(input('Input door (more or equal 3): '))
    ghost_index_1 = 0
    ghost_index_2 = 0
    print("Game - Ghost Game")
    print("\t There are N doors. Behind one there is ghost")
    print("\tYour task is not get the ghost")
    print("\t---Begining of the game---")
    while True:
        for i in range(door_count):
            print("____[" + str(i + 1) + "]", end = "" )
            print("____")
        user_choice = int(input("Your choice: "))
        ghost_index_1 = random.randint(1, door_count)
        ghost_index_2 = random.randint(1, door_count)
        while ghost_index_1 == ghost_index_2:
            ghost_index_2 = random.randint(1, door_count)
        for i in range(1,door_count+1):
            if i != ghost_index_1 and i != ghost_index_2:
                print("____[ ]", end="")
            else:
                print("____[G]",end="")
        if user_choice == ghost_index_1 or user_choice == ghost_index_2:
            print("\n--You lose!--")
            break
        else:
            user_score += 1
            print("\n--New round!--")
    again = str(input('\n\nYou want to play again? (Print Yes or No!)'))
    print("----------")
    print("Your score:" + str(user_score) + '\n')
print('GAME OVER')
