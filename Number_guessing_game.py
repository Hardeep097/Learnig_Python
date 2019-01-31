'''

                           This is just simple gussing game in Python. it is beginner's level game. NO proper validatons applied. 

'''

import random

i =0

while i == 0:
    randnum = random.randint(1,101)
        
    j = 0
    while j == 0:
        result = input("Guess number between 1 to 100: ")
        intresult = int(result)
        if randnum > intresult:
            print("The number is higher!")
        elif randnum < intresult:
             print("The number is lower!")
        else:
             print("Winner the number is:" + str(randnum))
             j = 1

    play = input("Press y to play or n to exit!")

    if play == "y":
        i = 0
    else:
        i = 1

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
