from random import random

picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]]

for row in picture:
    for x in row:
        if x == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

nota=int(input( ))
if 9 <= nota <= 10:
    print("Excelent")
elif 7 <=  nota <= 8:
    print("Bine")
elif 5 <=  nota <= 6:
    print("Suficient")
else:
    print("Reexaminare")

import random

nr = random.randint(1, 50)
print(nr)

import random

numar = random.randint(1, 50)
incercari=0
while True:
    guess = int(input("Ghicește numărul (1-50): "))

    if guess < numar:
        print("Numărul este mai mare!")
        incercari=incercari+1
    elif guess > numar:
        print("Numărul este mai mic!")
        incercari=incercari+1

    else:
        print("Felicitări! Ai ghicit!")
        print(incercari)
        break
