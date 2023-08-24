v = "yes"
while(v=="yes" or v=="Yes"):
    print("Please choose any one of these ['Rock','Paper','Scissors']")
    u1 = input()
    u2 = input()
    if u1==u2:
        print("Match is draw")
        continue
    elif u1=="rock" or u1=="Rock":
        if u2=="paper" or u2=="Paper":
            print("U2 Won")
        else:
            print("U1 Won")
    elif u1=="paper" or u1=="Paper":
        if u2=="Scissors" or u2=="scissors":
            print("U2 Won")
        else:
            print("U1 Won")
    elif u1=="scissors" or u1=="Scissors":
        if u2=="Rock" or u2=="rock":
            print("U2 Won")
        else:
            print("U1 Won")
    else:
        print("please, select the right option")
    v = input("If you like to play then type Yes, else No ")
