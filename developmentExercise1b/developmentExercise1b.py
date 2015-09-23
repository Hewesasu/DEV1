celc = input('What celcius is it today?\n')

while celc<0:
    celc = input('Celcius can not go under 0 celcius, enter again.\n')
kelvin = celc + 273.15

print kelvin,'Kelvin'