userInput = raw_input("Enter a sentence.\n")

lengthInput = len(userInput)
reversedWord = ""

for l in range(lengthInput, 0, -1):
    reversedWord += userInput[l-1]
print reversedWord

'''
#while loop version
    while lengthInput > 0:
        reversedWord += userInput[lengthInput -1]
        lengthInput = lengthInput - 1
    print reversedWord
'''

