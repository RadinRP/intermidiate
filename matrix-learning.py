board = [["_" , "_" , "_"],
         ["_" , "_" , "_"],
         ["_" , "_" , "_"]]
player = "x"
for i in range (9):
    row=int(input("enter the row"))
    col=int(input("enter the col"))
    board[row][col] = player
    print(board)
    if player == "x":
        player = "o"
    else :
        player = "x"