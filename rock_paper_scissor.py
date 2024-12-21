def rock_paper_scissor(num_1,num_2,bits_1,bits_2):
    p1=int(num_1[bits_1])%3
    p2=int(num_2[bits_2])%3
    if(player_1[p1]==player_2[p2]):
        print(" DRAW ")
    elif(player_1[p1]==0 and player_2[p2]==0):
        print(" PLAYER 2 WIN !! ")
    elif(player_1[p1]==1 and player_2[p2]==1):
        print(" PLAYER 2 WIN !! ")
    elif(player_1[p1]==0 and player_2[p2]==1):
        print(" PLAYER 1 WIN !! ")
    elif(player_1[p1]==1 and player_2[p2]==2):
        print(" PLAYER 1 WIN !! ")
    elif(player_1[p1]==2 and player_2[p2]==1):
        print(" PLAYER 1 WIN !! ")
    elif(player_1[p1]==2 and player_2[p2]==2):
        print(" PLAYER 2 WIN !! ")
player_1={0:"ROCK",1:"PAPER",2:"SCISSOR"}
player_2={0:"PAPER",1:"SCISSOR",2:"ROCK"}
while(True):
    num_1=input("PLAYER 1 , ENTER YOUR CHOICE :- ")
    num_2=input("PLAYER 1 , ENTER YOUR CHOICE :- ")
    bits_1=int(input("PLAYER 1 , ENTER YOUR SECREAT KEY :- "))
    bits_2=int(input("PLAYER 2 , ENTER YOUR SECREAT KEY :- "))
    rock_paper_scissor(num_1,num_2,bits_1,bits_2)
    ch=input("IF YOU WANT TO PLAY AGAIN THEN PRESS Y ELSE:- y/n :-")
    if ch=='n':
        break