def drawField(field):
    for row in range(5):
        if row%2 == 0:
            playingRow = int(row/2)
            for column in range(5):
                if column%2 == 0:
                    playingColumn = int(column/2)
                    if column != 4:
                        print(field[playingColumn][playingRow],end="")
                    else :
                        print(field[playingColumn][playingRow])
                else:
                    print("|",end="")   
        else:
            print("-----")
player = 1
currentBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
drawField(currentBoard)
turn = 0
while(turn <= 9):
    print("Player's turn: ",player)
    moveColumn = int(input("Enter the column: "))
    moveRow = int(input("Enter the row: ")) 
    if player == 1:
        if currentBoard[moveColumn][moveRow] == " ":
            currentBoard[moveColumn][moveRow] = "X"
            player = 2
            lastPlayer = 1
        elif currentBoard[moveColumn][moveRow] !=" ":
            turn -= 1                          
    else:
        if currentBoard[moveColumn][moveRow] == " ":
            currentBoard[moveColumn][moveRow] = "O"
            player = 1
            lastPlayer = 2
        elif currentBoard[moveColumn][moveRow] != " " :
            turn -= 1          
    turn+=1 
    if turn >= 5 :
        if (currentBoard[0][0] == currentBoard[1][0] == currentBoard[2][0] != " "): 
            drawField(currentBoard)
            print("Player",lastPlayer,"won")  
            break
        if (currentBoard[0][1] == currentBoard[1][1] == currentBoard[2][1] != " "):
            drawField(currentBoard)
            print("Player",lastPlayer,"won")     
            break
        if (currentBoard[0][2] == currentBoard[1][2] == currentBoard[2][2] != " " ):
            drawField(currentBoard)
            print("Player",lastPlayer,"won")     
            break
        if (currentBoard[0][2] == currentBoard[1][1] == currentBoard[2][0] != " " ):
            drawField(currentBoard)
            print("Player",lastPlayer,"won")     
            break
        if (currentBoard[0][0] == currentBoard[1][1] == currentBoard[2][2] != " " ):
            drawField(currentBoard)
            print("Player",lastPlayer,"won")     
            break
        if (currentBoard[0][0] == currentBoard[0][1] == currentBoard[0][2] != " " ):
            drawField(currentBoard)
            print("Player",lastPlayer,"won")     
            break
        if (currentBoard[1][0] == currentBoard[1][1] == currentBoard[1][2] != " " ):
            drawField(currentBoard)
            print("Player",lastPlayer,"won")     
            break
        if (currentBoard[2][0] == currentBoard[2][1] == currentBoard[2][2] != " " ):
            drawField(currentBoard)
            print("Player",lastPlayer,"won")     
            break
        else:
            if turn == 9:
                drawField(currentBoard)
                print("NO WIN")
                break        
    drawField(currentBoard)
  
