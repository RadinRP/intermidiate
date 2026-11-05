board = [ ["_" ,"_" ,"_" ,"_"],
          ["_" ,"_" ,"_" ,"_"],
          ["_" ,"_" ,"_" ,"_"], 
          ["_" ,"_" ,"_" ,"_",]]

player = {
    "name" : "abdolah",
    "health" : 3 ,
    "coin" : 10 , 
    "move" : 0
    }

p_row = 0
p_col = 0
treasure_row = 3
treasure_col = 3

while True:
    for row in range (4):
        for col in range (4):
            if (row == p_row and col == p_col):
                print("p" , end = " ")
            else:
                print("." , end = " ")
        print()

    p_move = str(input("where you want to go with W , D ,S , A : ")).upper()
    new_row = p_row
    new_col = p_col

    if (p_move == "W"):
        new_row -= 1
    elif (p_move == "D"):
        new_col += 1
    elif (p_move == "S"):
        new_row += 1
    elif (p_move == "A"):
        new_col -= 1
    else:
        print("invalied input")
    if ( 0 <= new_row < 4 and 0 <= new_col < 4):
        p_row = new_row
        p_col = new_col
        player["move"] = player["move"] + 1
    if (p_row == treasure_row and p_col == treasure_col):
        player["coin"] += 100
        print("you won")
        break