import random

rndnr = random.randrange(0, 20)

print ("I have a secret number, guess what it is!")

guessvalue = int(input())

while guessvalue != rndnr:

    if guessvalue > rndnr:
        print ("To high, Try again")
    elif guessvalue < rndnr:
        print("To low, try again")

    guessvalue = int(input())   

print ("Correct!!!")

    

    
    



