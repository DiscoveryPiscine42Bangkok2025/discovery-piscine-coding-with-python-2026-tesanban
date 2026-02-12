
def check_queen_attack(board, start_y, start_x): # Queen
    direc = [(0,1),(0,-1),(-1,0),(1,0),  # Rook
             (1,1),(-1,-1),(1,-1),(-1,1)] #bishop
             
    rows = len(board)      
    cols = len(board[0])   

    for dy, dx in direc:
        curr_y, curr_x = start_y, start_x
        while True:
            curr_y += dy
            curr_x += dx
            if not (0 <= curr_y < rows and 0 <= curr_x < cols):
                break
            target = board[curr_y][curr_x]
            
            if target == "K":     # เจอ King!
                return True    
            
            elif target != ".":

                break
        
    return False

def check_Rook_attack(board, start_y, start_x): # Rook
    direc = [(0,1),(0,-1),(-1,0),(1,0)] # Rook
             
    rows = len(board)      
    cols = len(board[0])   

    for dy, dx in direc:
        curr_y, curr_x = start_y, start_x
        while True:
            curr_y += dy
            curr_x += dx
            if not (0 <= curr_y < rows and 0 <= curr_x < cols):
                break
            target = board[curr_y][curr_x]
            
            if target == "K":     # เจอ King!
                return True    
            
            elif target != ".":

                break
        
    return False

def check_Bishop_attack(board, start_y, start_x): # Queen
    direc =  [(1,1),(-1,-1),(1,-1),(-1,1)] #bishop
             
    rows = len(board)      
    cols = len(board[0])   

    for dy, dx in direc:
        curr_y, curr_x = start_y, start_x
        while True:
            curr_y += dy
            curr_x += dx
            if not (0 <= curr_y < rows and 0 <= curr_x < cols):
                break
            target = board[curr_y][curr_x]
            
            if target == "K":     # เจอ King!
                return True    
            
            elif target != ".":

                break
        
    return False

def squard(board):
    if not board or len(board) != len(board[0]):
        print("Not Square!")

