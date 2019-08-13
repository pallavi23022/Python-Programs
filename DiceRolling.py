print("This is a Dice Rolling program")
leave=0
while leave!="q":

    import random

    
    print("Press enter to roll")

    input() # after you press enter it will trigger input function if you will not write
       #it you will not be able to press enter it will just roll on its own automatically

    number=random.randint(1,6)


    if number==1:
        print("[----------]")
        print("[          ]")
        print("[     O    ]")
        print("[          ]")
        print("[----------]")
        print()
        print("Press 'Q' to Quit")
        leave=input() 
    if number==2:
        print("[----------]")
        print("[          ]")
        print("[   O   O  ]")
        print("[          ]")
        print("[----------]")
        print()
        print("Press 'Q' to Quit")
        leave=input()
    if number==3:
        print("[----------]")
        print("[          ]")
        print("[  O  O  O ]")
        print("[          ]")
        print("[----------]")
        print()
        print("Press 'Q' to Quit")
        leave=input()
    if number==4:
        print("[----------]")
        print("[  O   O   ]")
        print("[          ]")
        print("[  O   O   ]")
        print("[----------]")
        print()
        print("Press 'Q' to Quit")
        leave=input()
    if number==5:
        print("[----------]")
        print("[   O   O  ]")
        print("[     O    ]")
        print("[   O   O  ]")
        print("[----------]")
        print()
        print("Press 'Q' to Quit")
        leave=input()
    if number==6:
        print("[----------]")
        print("[   O   O  ]")
        print("[   O   O  ]")
        print("[   O   O  ]")
        print("[----------]")
        print()
        print("Press 'Q' to Quit")
        leave=input()


