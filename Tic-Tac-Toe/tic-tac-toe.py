#Tic-Tac-Toe Game in Python

#Taking a 2-D List to store the X and O
mainboard: list[list[str]]=[[" "," "," "],[" "," "," "],[" "," "," "]]

#Check Horizontal Winning Position
def horizontalCheck() -> bool:
    """horizontalCheck Check Horizontal Winning Condition

    Returns:
        bool: If getting a horizontal win then returns True else returns False
    """
    for i in range(len(mainboard)):
        if(mainboard[i].count(mainboard[i][0])==3 and mainboard[i][0]!=" "):
            return True
    return False

#Check Vertical Winning Position
def verticalCheck() -> bool:
    """verticalCheck Check Vertical Winning Condition

    Returns:
        bool: If getting a vertical win then returns True else returns False
    """
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

#Check Diagonal Winning Position
def diagonalCheck() -> bool:
    """diagonalCheck Perform Winning Condition Check for Diagonals

    Returns:
        bool: If Winning in left to right or vice versa diagonals then return True else return False
    """
    #left to right diagonal check
    flag=0
    for i in range(3):
        for j in range(3):
            if(i==j):
                if(mainboard[i][j]==mainboard[0][0] and mainboard[0][0]!=" "):
                    pass
                else:
                    flag=1
                    break
            else:
                continue
        if(flag==1):
            break
    if(flag==0):
        return True
    #right to left diagonal check
    flag=0
    for i in range(3):
        for j in range(3):
            if(i+j==2):
                if(mainboard[i][j]==mainboard[0][2] and mainboard[0][2]!=" "):
                    pass
                else:
                    flag=1
                    break
        if(flag==1):
            break
    if(flag==0):
        return True
    else:
        return False

#Check Draw Status
def drawCheck() -> bool:
    """drawCheck This Function is to check the DRAW condition for the game

    Returns:
        bool: If there are no position to fill in the main board then it results in draw condition hence returns True otherwise it returns False
    """
    for i in range(3):
        for j in range(3):
            if(mainboard[i][j]==" "):
                return False
    return True

#Position Input Check Function
def inputcheck(position: str) -> bool:
    """inputcheck Perform InputCheck for the Position

    Args:
        position (str): Position string for input to mainboard

    Returns:
        bool: returns True if the input position is correct and falls on the board position range
              returns False if the input position is not correct or the position is already filled.
    """
    l1: list[str]=position.split(" ")
    for i in l1:
        if(int(i)>3 or int(i)<1):
            return True
    if (mainboard[int(l1[0])-1][int(l1[1])-1]!=" "):
        return True
    return False

#Place the Sign in the Board
def placesign(position: str, sign: str) -> None:
    """placesign This Function is used to input the Player Sign to mainboard

    Args:
        position (str): Position string to input in mainboard
        sign (str): Character to input in the mainboard
    """
    l1: list[str]=position.split(" ")
    mainboard[int(l1[0])-1][int(l1[1])-1]=sign

#Printing the Board
def displayboard() -> None:
    """displayboard This Function is created to Display the MainBoard
    """
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
player1name: str=input("Enter Player 1 Name :")
player2name: str=input("Enter Player 2 Name :")
flag=1
while (True):
    if (flag==1):
        player1: str=input("\n"+player1name+"'s Turn, Enter the position in the board for \" X \" :")
        while(inputcheck(player1)):
            player1=input("Wrong Position Entered !!\nEnter the position again in the board for \" X \" :")
        placesign(player1,"X")
        flag=0
    else:
        player2: str=input("\n"+player2name+"'s Turn, Enter the position in the board for \" O \" :")
        while(inputcheck(player2)):
            player2=input("Wrong Position Entered !!\nEnter the position again in the board for \" O \" :")
        placesign(player2,"O")
        flag=1
    print()
    displayboard()
    print()
    # Winning Check (Horizontal Wins | Vertical Wins | Diagonal Wins | Draw Check)
    if(horizontalCheck() or verticalCheck() or diagonalCheck()):
        if(flag==0):
            print(player1name,"Wins!")
        else:
            print(player2name,"Wins!")
        break
    elif(drawCheck()):
        print("Its a DRAW! between %s and %s."%(player1name,player2name))
        break
    else:
        continue
