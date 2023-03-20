n=int(input())
currRow=1
while currRow<=n:
    spaces=1
    while spaces<=n-currRow:
        print(" ",end="")
        spaces+=1
    currCol=currRow
    while currCol<=(2*currRow)-1:
        print(currCol,end="")
        currCol+=1
    currCol = 2*(currRow-1)
    while currCol >= currRow:
        print(currCol,end="")
        currCol-=1
    print()
    currRow+=1

# Output -
#       1
#     2 3 2
#   3 4 5 4 3
# 4 5 6 7 6 5 4      