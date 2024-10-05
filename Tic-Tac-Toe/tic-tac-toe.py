#Tic-Tac-Toe Game in Python

#Taking a 2-D List to store the X and O
mainboard=[[" "," "," "],[" "," "," "],[" "," "," "]]

#Printing the Board
def displayboard(board):
    for i in range(len(board)):
        for j in board[i]:
            print(j," | ",sep="",end="")
        if i<2:
            print("\b\b \n- - - - -")
        else:
            print("\b\b ")

#Game Output Screen
print("-----------------------------")
print("Welcome to TIC-TAC-TOE Game!!")
print("-----------------------------")
print("Rule: Enter the below Board position values (without space) to enter your sign in the board :\n")
for i in range(1,4):
    for j in range(1,4):
        print(str(i)+str(j)," | ",sep="",end="")
    if i<3:
        print("\b\b \n- - - - - - -")
    else:
        print("\b\b ")
print("\nEnjoy the game !!")
print("-----------------------------")
player1name=input("Enter Player 1 Name :")
player2name=input("Enter Player 2 Name :")
player1=input("\n"+player1name+"'s Turn, Enter the position in the board for \" X \" :")