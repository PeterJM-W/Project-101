import random
   
rolls = 0
score = 0
option = input("Do you want to roll a dice? (y/n): ")
while option != 'y':
    if option =='n':
        print("Wrong answer.")
        print("Try again. :)")
    
    if option != 'y' and option !='n':
        print("Invalid input")
        print("Please use y (for yes) or n (for no)")
        
    option = input("Do you want to roll a dice? (y/n): ")

while option == 'y':   
    n = random.randint(1, 6)
    if n==1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if n==2:
        print("[-----]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[-----]")
    if n==3:
        print("[-----]")
        print("[ 0   ]")
        print("[  0  ]")
        print("[   0 ]")
        print("[-----]")
    if n==4:
        print("[-----]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[-----]")
    if n==5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if n==6:
        print("[-----]")
        print("[ 000 ]")
        print("[     ]")
        print("[ 000 ]")
        print("[-----]")
    
    rolls += 6
    score += int(n)
    option = input("Do you want to roll again? (y/n): ")
    while option != 'y' and option != 'n':
        input("Please use y (for yes) or n (for no): ")
    
    if option == 'n':
        print("Your score was", score, "/", rolls)
        if (rolls == score) and (rolls > 6):
            print("Congratulations! You won! You have great luck!")
        elif rolls == score:
            print("You did amazing but take a chance!")
        elif ((rolls) / 2) < score:
            print("Well done! You've done quite well")
        else:
            print("Good try. Better luck next time...")
    