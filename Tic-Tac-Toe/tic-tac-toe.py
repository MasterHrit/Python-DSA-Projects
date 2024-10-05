#Tic-Tac-Toe Game in Python

#Taking a 2-D List to store the X and O
mainboard=[[" "," "," "],[" "," "," "],[" "," "," "]]

#Check Horizontal Winning Position
def horizontalCheck():
    for i in range(len(mainboard)):
        if(mainboard[i].count(mainboard[i][0])==3 and mainboard[i][0]!=" "):
            return True
    return False

#Check Vertical Winning Position
def verticalCheck():
    for i in range(len(mainboard[0])):
        flag=0
        for j in range(3):
            if(mainboard[j][i]==mainboard[0][i] and mainboard[0][i]!=" "):
                pass
            else:
                flag=1
        if(flag==0):
            return True
    return False

#Position Input Check Function
def inputcheck(position):
    l1=position.split(" ")
    for i in l1:
        if(int(i)>3 or int(i)<1):
            return True
    if (mainboard[int(l1[0])-1][int(l1[1])-1]!=" "):
        return True
    return False

#Place the Sign in the Board
def placesign(position, sign):
    l1=position.split(" ")
    mainboard[int(l1[0])-1][int(l1[1])-1]=sign

#Printing the Board
def displayboard():
    for i in range(len(mainboard)):
        for j in mainboard[i]:
            print(j," | ",sep="",end="")
        if i<2:
            print("\b\b \n- - - - -")
        else:
            print("\b\b ")

#Game Output Screen
print("-----------------------------")
print("Welcome to TIC-TAC-TOE Game!!")
print("-----------------------------")
print("Rule: Enter the below Board position values (with space) to enter your sign in the board :\n")
for i in range(1,4):
    for j in range(1,4):
        print("["+str(i)+" "+str(j)+"]"," | ",sep="",end="")
    if i<3:
        print("\b\b \n- - - - - - - - - - -")
    else:
        print("\b\b ")
print("\nEnjoy the game !!")
print("-----------------------------")
player1name=input("Enter Player 1 Name :")
player2name=input("Enter Player 2 Name :")
flag=1
while (True):
    if (flag==1):
        player1=input("\n"+player1name+"'s Turn, Enter the position in the board for \" X \" :")
        while(inputcheck(player1)):
            player1=input("Wrong Position Entered !!\nEnter the position again in the board for \" X \" :")
        placesign(player1,"X")
        flag=0
    else:
        player2=input("\n"+player2name+"'s Turn, Enter the position in the board for \" O \" :")
        while(inputcheck(player2)):
            player2=input("Wrong Position Entered !!\nEnter the position again in the board for \" O \" :")
        placesign(player2,"O")
        flag=1
    print()
    displayboard()
    print()
    # Winning Check (Horizontal Wins | Vertical Wins | Diagonal Wins | Draw Check)
    if(horizontalCheck() or verticalCheck()):
        if(flag==0):
            print(player1name,"Wins!")
        else:
            print(player2name,"Wins!")
        break
    else:
        continue