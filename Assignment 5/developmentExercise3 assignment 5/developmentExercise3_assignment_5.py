userInput = raw_input("Enter password to encrypt!\n")
userInputNum = raw_input("Enter a number for encryption!\n")

s = int(userInputNum)
output = ""

while s > 26 or s < -26:
        if s > 26:
            s -= 26
        elif s < -26:
            s += 26

for x in userInput:
    num = ord(x) + s
    if str.isalpha(x):
        if x.islower():
            if num > 122:
                num -= 26
            elif num < 97:
                num += 26
        else:
            if num > 90:
                num -= 26
            elif num < 65:
                num += 26
        output += chr(num)
    else:
        output += x
print "new password: ", output

