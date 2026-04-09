import random
x=random.randint(1,100)
print(x)

userGuess=int(input("Pick a number from 1 to a 100: "))

while userGuess!=x:
    print("Try again")
    userGuess=int(input("Pick a number from 1 to a 100: "))
else:
    print('Good job')