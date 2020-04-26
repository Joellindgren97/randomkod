import random
import time
import os

os.system('clear')
print("Nu kör vi sten, sax, påse!!! bäst av 3")
time.sleep(1)
print("Skriv in ditt val:")

val_list = ['sten', 'sax', 'pose']

datorpoint = 0
personpoint = 0

while True:

    rnd = random.choice(val_list)
    mittval = input()
    
    if (mittval == "sten") or (mittval == "sax") or (mittval == "pose"):

        print("Jag väljer - ", rnd)    
        if mittval == rnd:
            print("Samma!!", datorpoint, "-", personpoint)

        elif mittval != rnd:
            if ((mittval == "sten") and (rnd == "sax")) or ((mittval == "pose") and (rnd == "sten")) or ((mittval == "sax") and (rnd == "pose")):
                personpoint = personpoint+1
                print("Du vann!!", datorpoint, "-", personpoint)

            elif ((mittval == "sax") and (rnd == "sten")) or ((mittval == "sten") and (rnd == "pose")) or ((mittval == "pose") and (rnd == "sax")):
                datorpoint = datorpoint+1
                print("Jag vann!!", datorpoint, "-", personpoint)

    else:
        print("Fel inmatning, prova igen")

    if datorpoint == 3:
        print ("Jag vann, EZZ")
        break
    elif personpoint == 3:
        print ("Du vann, Grattis!!")
        break