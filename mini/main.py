from checkmate import *
board = """\
B.R.
..K.
....
..P.\
"""


rows = board.strip().splitlines()
array = [list(row) for row in rows]
checkboardY = len(array)
k_count = 0           
found_attack = False  
board_valid = True 
if checkboardY == 0:
    board_valid = False
else:
    for row in array:
        if len(row) != checkboardY:
            board_valid = False
            break

if not board_valid:
    print("Fail")  

else: 
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

            elif piece == "K": 
                k_count += 1
            
            elif piece == ".":
                pass
            
            else:
                board_valid = False 

    
    if k_count != 1:
        board_valid = False

    
    if board_valid and found_attack:
        print("Success")
    else:
        print("Fail")