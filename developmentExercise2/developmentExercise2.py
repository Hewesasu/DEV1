userInput = input("1:Rock, 2:paper or 3:scissors?\n")

while userInput > 3 or userInput < 1:
    userInput = input("Choose between 1-3 for 1:Rock, 2:paper or 3:scissors\n")

while userInput != 4:

    from random import randint
    program = randint(1,3)

    if userInput == 1:
        if program == 1:
            print('User choose "Rock"\nProgram choose "Rock"\nDraw!')
        elif program == 2:
            print('User choose "Rock"\nProgram choose "Paper"\nPaper beats Rock, Program Wins!')
        elif program == 3:
            print('User choose "Rock"\nProgram choose "Scissors"\nRock beats scissors, Player Wins!')
    elif userInput == 2:
        if program == 1:
            print('User choose "Paper"\nProgram choose "Rock"\nPaper beats Rock, Player Wins!')
        elif program == 2:
            print('User choose "Paper"\nProgram choose "Paper"\nDraw!')
        elif program == 3:
            print('User choose "Paper"\nProgram choose "Scissors"\nScissors beats paper, Program Wins!')
    elif userInput == 3:
        if program == 1:
            print('User choose "Scissors"\nProgram choose "Rock"\nRock beats scissors, Program Wins!')
        elif program == 2:
            print('User choose "Scissors"\nProgram choose "Paper"\nScissors beats paper, Player Wins!')
        elif program == 3:
            print('User Choose "Scissors"\nProgram choose "Scissors"\nDraw!')
    userInput = input("Choose between 1-3 to play again or choose 4 to quite.\n")

