import random
door=[0,0,0]
goatdoor=[]
swap=0
dontswap=0
j=0
while j<10:
    x=random.randint(0,2)
    door[x]="BMW"
    for i in range(0,3):
        if i==x:
            continue
        else:
            door[i]="GOAT"
            goatdoor.append("GOAT")
    choice=int(input("ENTER YOUR CHOICE :- "))
    door_open=random.choice(goatdoor)
    while door_open==choice:
        door_open=random.choice(goatdoor)
    ch=input("YOU WANT TO SWAP ! Y/N ")
    if ch=='y':
        if door[choice]=='GOAT':
            print("PLAYER WIN !!")
            swap+=1
        else:
            print(" PLAYER LOST !!")
    else:
        if door[choice]=='GOAT':
            print("PLAYER LOST !!")
        else:
            print(" PLAYER WIN !!")
            dontswap+=1
    j+=1
print(swap)
print(dontswap)
