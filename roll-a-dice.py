import random
   
option = "y"
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

    option = input("Do you want to roll a dice? (y/n): ")