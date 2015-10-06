userInput = raw_input("Enter your password.\n")

lengthInput = len(userInput)
lowCase = False
upperCase = False
digit = False
special = False
securityCounter = 0

for l in range(lengthInput -1):
    character = userInput[l]
    if character.islower():
        lowCase = True
    elif character.isupper():
        upperCase = True
    elif character.isdigit():
        digit = True
    elif character.isalpha() == False:
        special = True
'''
#while loop version
    while lengthInput > 0:
        character = userInput[lengthInput -1]
        if character.islower():
            lowCase = True
        elif character.isupper():
            upperCase = True
        elif character.isdigit():
            digit = True
        elif character.isalpha() == False:
            special = True
        lengthInput -= 1
'''

if len(userInput) >= 6 and len(userInput) <= 12:
    securityCounter += 1
elif len(userInput) > 12:
    securityCounter += 2
if lowCase == True:
    securityCounter += 1
if upperCase == True:
    securityCounter += 1
if digit == True:
    securityCounter += 1
if special == True:
    securityCounter += 1


if securityCounter <= 2:
    print("security level is low!")
elif securityCounter == 3:
    print("security level is medium.")
elif securityCounter == 4:
    print("security level is strong.")
elif securityCounter == 5:
    print("security level is very strong!")
print securityCounter
