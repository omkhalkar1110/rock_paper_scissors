import random
computer=random.choice(["rock","paper","scissors"])
you=input("ENTER YOUR CHOICE \n  r for ROCK\n s for SCISSORS \n p for PAPER\n")
youdict={"r":"rock", "p":"paper", "s":"scicors"}
out=youdict[you]

if(computer==out):
    print("ITS A DRAW !!!")
else:
    if(computer=="rock" and out=="paper"):
        print("YOU WINN!!!!")   
    elif(computer=="rock" and out=="scissors"):
        print("YOU LOSE") 

    elif(computer=="paper" and out=="rock"):
        print("YOU LOSE!!!")
    elif(computer=="paper" and out=="scissors"):
        print("YOU WIN!!!")

    elif(computer=="scissors" and out=="rock"):
        print("YOU WIN!!!")
    elif(computer=="scissors" and out=="paper"):
        print("YOU LOSE!!!")
   
    






