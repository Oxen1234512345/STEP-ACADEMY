import random
print ("Welcome to the game: 'Rock,Paper,Scissors")
print ("\t The Game will go against the computer")
again = 'Yes'
while again == 'Yes':
    print ("\t The game consists of 3 rounds.")
    print("\t Winner is one with more points")
    print("\t Use big Letters to select")
    print("\t\t [R] - rock")
    print("\t\t [P] - paper")
    print("\t\t [SC] - scissors")
    print("\t\t [L] - lizard")
    print("\t\t [SP] - spock")
    user_score = 0
    user_choice = 0
    bot_score = 0
    bot_choice = 0
    print ("-----Begining of the game-----")

    for i in range(3):
        print("-----Round-----" + str(i+1) + "-----")
        user_choice = input("Your choice: ")
        bot_choice = random.choice(["R", "SP", "L", "SC", "P"])
        print("Your choice: " + user_choice + " x Bot choice " + bot_choice)
        if user_choice == bot_choice:
            print('Draw')
        elif user_choice == 'R':
            if bot_choice == 'SC' or 'L':
                user_score += 1
                print("User won the round")
            else:
                bot_score += 1
                print("Bot won the round")
        elif user_choice == 'SC':
            if bot_choice == 'P' or 'L':
                user_score += 1
                print("User won the round")
            else:
                bot_score += 1
                print("Bot won the round")
        elif user_choice == 'P':
            if bot_choice == 'R' or 'SP':
                user_score += 1
                print("User won the round")
            else:
                bot_score += 1
                print("Bot won the round")
        elif user_choice == 'L':
            if bot_choice == 'SP' or 'P':
                user_score += 1
                print("User won the round")
            else:
                bot_score += 1
                print("Bot won the round")
        elif user_choice == 'SP':
            if bot_choice == 'SC' or 'R':
                user_score += 1
                print("User won the round")
            else:
                bot_score += 1
                print("Bot won the round")
        else:
            print("Error")
    if user_score > bot_score:
        print("User win")
    elif user_score < bot_score:
        print("Bot win")
    else:
        print("Draw")
    again = str(input('\n\nYou want to play again? (Print Yes or No!)'))
print('GAME OVER')