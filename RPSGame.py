import random


def ComputerPick ():
    return random.randrange(1,4)
ComputerPick ()

ComputerNo = ComputerPick()

def Userpick (ComputerNo):
    print("Lets play rock, paper and scissors")
    print("1. Rock")
    print("2. paper")
    print("3. Scissors")
    print("Use the number to select your choice")
    PickedNo = int(input())

    print("Computer Picked" , (ComputerNo))

    if PickedNo == 1 and ComputerNo == 2 :
        print(" Paper Covers Rock . You loose")
    elif PickedNo == 1 and ComputerNo == 3 :
        print(" Rock Crushed scissors. You win!")
    elif PickedNo == 1 and ComputerNo == 1 :
        print(" Draw . Lets run again")
    elif PickedNo == 2 and ComputerNo == 1 :
        print(" Paper Covers Rock . You win")
    elif PickedNo == 2 and ComputerNo == 2 :
        print(" Draw . Lets run again")
    elif PickedNo == 2 and ComputerNo == 3 :
        print(" Scissors cuts paper . You loose")
    elif PickedNo == 3 and ComputerNo == 1 :
        print(" Rock crushes Scissors . You loose")
    elif PickedNo == 3 and ComputerNo == 2 :
        print(" Scissors cuts paper . You win")
    elif PickedNo == 3 and ComputerNo == 3 :
        print("Draw . Lets run again")
    else :
        print(" pick from 1 -3")
        
Userpick (ComputerNo)











