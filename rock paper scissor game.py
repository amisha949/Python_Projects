import random
print("Rock paper scissor game")
c=0
cn=0
while True:
    user=input("Choose rock paper scissor=")
    print("User's choice=",user)
    comp=random.randint(1,3)
    if(comp==1):
        cc="rock"
    elif(comp==2):
        cc="paper"
    else:
        cc="scissor"
    print("Computer's choice=",cc)
    if(user==cc):
        print("Its a tie")
    elif(user=="rock"):
        if(cc=="paper"):
            print("Computer won")
            cn=cn+1
        else:
            print("You won")
            c=c+1
    elif(user=="paper"):
        if(cc=="rock"):
            print("You won")
            c=c+1
        else:
            print("Computer won")
            cn=cn+1
    elif(user=="scissor"):
        if(cc=="rock"):
            print("Computer won")
            cn=cn+1
        else:
            print("You won")
            c=c+1
    next=input("Do you want to continue the game yes or no=")
    if(next!="yes" and next!="no"):
        print("Wrong input")
        break
    elif(next=="no"):
        break
print("Game completed")
print(f"Computer won {cn} game")
print(f"You won {c} game")
