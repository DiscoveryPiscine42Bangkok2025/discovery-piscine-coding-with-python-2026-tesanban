from checkmate import *
board = """\
R...
.K..
..P.
...K\
"""

check = True

rows = board.strip().splitlines()
k_count = 0
    

array = [list(row) for row in rows]
for row in array:
    print(row)




for y in range(0,len(array)):
        for x in range(0,len(array[y])):
            if k_count > 1:
                check = False
                print("The King Should be one!!")
                if check == False:
                    break

            if array[y][x] == "Q":
                if check_queen_attack(array, y, x):
                    check = True

            elif array[y][x] == "B":
                if check_Bishop_attack(array, y, x):
                    check = True
            elif array[y][x] == "R":
                if check_Rook_attack(array, y, x):
                    check = True
            elif array[y][x] == "P" :
                if check_Pawn_attack(array, y, x):
                    check = True
            elif array[y][x] == "." or "K":
                if array[y][x] == "K":
                    k_count += 1
                
            else:
                check = False
                print("Error")
        if k_count == 0:
            check = False
            print("Where ur King!!")
        if k_count == 1:
            check = False

        if check == True:
            print("Success")
else:
        check == False
        print("Fail")



                    


