from checkmate import array
check = False

for y in range(0,len(array)):
    for x in range(0,len(array[y])):
        if(array[y][x] == "P"): # เบี้ย
            if(array[y-1][x-1] == "K"):
                check = True
            elif(array[y-1][x+1] == "K"):
                check = True

        elif(array[y][x] == "R"): #เรื่อ
            for n in range(x+1,len(array[y]),1): #ด้านขวาอย่างเดียว
                if(array[y][n]) == "K":
                    check = True
            for nn in range(x-1,-1,-1):#ด้านซ้าย
                if(array[y][nn]) == "K":
                    check = True
print(check)

                    


