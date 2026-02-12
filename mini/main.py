from checkmate import *
board = """\
R...
.K..
..P.
....\
"""

rows = board.strip().splitlines()
array = [list(row) for row in rows]
checkboardY = len(array)
k_count = 0           
found_attack = False  
board_valid = True 

for row in array:
    print(row)
if checkboardY == 0:
    board_valid = False
else:
    for row in array:
        if len(row) != checkboardY:
            board_valid = False
            print("Error: Board is not a square!")
            break 

for y in range(len(array)):
    for x in range(len(array[y])):
            
        piece = array[y][x]

        
        if piece == "Q":
            if check_queen_attack(array, y, x):
                found_attack = True
        
        elif piece == "B":
            if check_Bishop_attack(array, y, x):
                found_attack = True
                
        elif piece == "R":
            if check_Rook_attack(array, y, x):
                found_attack = True
                
        elif piece == "P":
             if check_Pawn_attack(array, y, x):
                 found_attack = True

        
        elif piece in [".", "K"]:
            if piece == "K":
                k_count += 1
        
        else:
            board_valid = False


if k_count != 1:
    board_valid = False
    print(f"THE King should Be One!")


if board_valid:
    if found_attack:
        print("Success") 
    else:
        print("Fail")    
else:
    
    print("Fail") #king have 2 what ???