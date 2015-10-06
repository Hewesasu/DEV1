import math
option = input("choose a number between 1/4\n 1: full square\n 2: hallow square\n 3: rectangle triangle\n 4: isosceles triangle\n 5: fullCircle\n 6: smiley\n")
size = input("Enter a number for the size.\n")

figure = ""

def fullSquare(size, figure):
    for h in range(size):
        for w in range(size):
           figure += "*"
        figure += "\n"
    return figure

def hallowSquare(size, figure):
    for h in range(size):
        for w in range(size):
            if h == 0 or h == size -1 or w == 0 or w == size -1:
                figure += "*"
            else:
                figure += " "
        figure += "\n"
    return figure

def fullRecTriangle(size, figure):
    for h in range(size):
        for w in range(h+1):
                figure += "*"
        figure += "\n"
    return figure
'''
# if size is 5, it will print *1, *3, *5
def fullIsoTrijangle(size, figure):
    for h in range(size+1):
        if h % 2 == 1:
            for s in range((size - h) / 2):
                figure += " "
            for w in range(h):
                figure += "*"
            figure += "\n"
    return figure

# if size is 5, it will print *1, *3, *5, *7, *9
def fullIsoTrinangle(size, figure):
    a = 1 
    for h in range(size):
       for s in range(((size*2-1) - a) / 2): 
           figure += "."
       for w in range(a):
           figure += "*"
       for s in range(((size*2-1) - a) / 2): 
           figure += "."
       a += 2
       figure += "\n"
    return figure
'''
def fullIsoTriangle(size, figure):
    a = 1 
    for h in range(size):
       for s in range(size*2-1):
           if s >= ((size*2-1) - a) / 2 and s < (((size*2-1) - a) / 2) + a:
               figure += "*"
           else:
               figure += "."
       a += 2
       figure += "\n"
    return figure

def fullCircle(size, figure):
    r = size/2 
    for x in range(size):
        dx = x - r
        for y in range(size):
            dy = y - r
            if math.sqrt(dx**2+dy**2) < r:
                figure += "*"
            else:
                figure += " "
        figure += "\n"
    return figure

def smiley(size, figure):
    r = size/2 
    for x in range(size):
        dx = x - r
        for y in range(size):
            dy = y - r
            if math.sqrt(dx**2+dy**2) < r and math.sqrt(dx**2+dy**2) + 1 > r:
                figure += "*"
            else:
                figure += " "
        figure += "\n"
    return figure

if option == 1:
    output = fullSquare(size, figure)
elif option == 2:
    output = hallowSquare(size, figure)
elif option == 3:
    output = fullRecTriangle(size, figure)
elif option == 4:
    output = fullIsoTriangle(size, figure)
elif option == 5:
    output = fullCircle(size, figure)
elif option == 6:
    output = smiley(size, figure)

print "\n", output