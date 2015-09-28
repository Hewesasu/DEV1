def validating(input):
    newInput = input
    while newInput.isdigit() == False:
        newInput = raw_input("Invalid input, choose between 1-5!\n")
    return int(newInput)

userInput = raw_input("1:Rock, 2:paper, 3:scissors, 4:lizard, 5:spock?\n")
userInput = validating(userInput)

while userInput > 5 or userInput < 1:
            userInput = raw_input("Choose between 1-5 for 1:Rock, 2:paper, 3:scissors, 4:lizard, 5:spock\n")
            userInput = validating(userInput)

while userInput != 9:

    from random import randint
    program = randint(1,5)

    if userInput == 1:
        if program == 1:
            print('User choose "Rock"\nProgram choose "Rock"\nDraw!')
        elif program == 2:
            print('User choose "Rock"\nProgram choose "Paper"\nPaper beats Rock, Program Wins!')
        elif program == 3:
            print('User choose "Rock"\nProgram choose "Scissors"\nRock beats scissors, Player Wins!')
        elif program == 4:
            print('User choose "Rock"\nProgram choose "Lizard"\nRock beats lizard, Player Wins!')
        elif program == 5:
            print('User choose "Rock"\nProgram choose "Spock"\nSpock beats Rock, Program Wins!')
    elif userInput == 2:
        if program == 1:
            print('User choose "Paper"\nProgram choose "Rock"\nPaper beats Rock, Player Wins!')
        elif program == 2:
            print('User choose "Paper"\nProgram choose "Paper"\nDraw!')
        elif program == 3:
            print('User choose "Paper"\nProgram choose "Scissors"\nScissors beats paper, Program Wins!')
        elif program == 4:
            print('User choose "Paper"\nProgram choose "Lizard"\nLizard beats paper, Program Wins!')
        elif program == 5:
            print('User choose "Paper"\nProgram choose "Spock"\nPaper beats spock, Player Wins!')
    elif userInput == 3:
        if program == 1:
            print('User choose "Scissors"\nProgram choose "Rock"\nRock beats scissors, Program Wins!')
        elif program == 2:
            print('User choose "Scissors"\nProgram choose "Paper"\nScissors beats paper, Player Wins!')
        elif program == 3:
            print('User Choose "Scissors"\nProgram choose "Scissors"\nDraw!')
        elif program == 4:
            print('User choose "Scissors"\nProgram choose "Lizard"\nSciccors beats lizard, Player Wins!')
        elif program == 5:
            print('User choose "Scissors"\nProgram choose "Spock"\nSpock beats scissors, Program Wins!')
    elif userInput == 4:
        if program == 1:
            print('User choose "Lizard"\nProgram choose "Rock"\nRock beats lizard, Program Wins!')
        elif program == 2:
            print('User choose "Lizard"\nProgram choose "Paper"\nLizard beats paper, Player Wins!')
        elif program == 3:
            print('User Choose "Lizard"\nProgram choose "Scissors"\nScissors beats lizard, Program Wins!')
        elif program == 4:
            print('User choose "Lizard"\nProgram choose "Lizard"\nDraw!')
        elif program == 5:
            print('User choose "Lizard"\nProgram choose "Spock"\nLizard beats spock, Player Wins!')
    elif userInput == 5:
        if program == 1:
            print('User choose "Spock"\nProgram choose "Rock"\nSpock beats rock, Player Wins!')
        elif program == 2:
            print('User choose "Spock"\nProgram choose "Paper"\nPaper beats spock, Program Wins!')
        elif program == 3:
            print('User Choose "Spock"\nProgram choose "Scissors"\nSpock beats scissors, Player Wins!')
        elif program == 4:
            print('User choose "Spock"\nProgram choose "Lizard"\nLizard beats spock, program Wins!')
        elif program == 5:
            print('User choose "Spock"\nProgram choose "Spock"\nDraw!')
    userInput = raw_input("Choose between 1-5 to play again or choose 9 to quite.\n")
    userInput = validating(userInput)

