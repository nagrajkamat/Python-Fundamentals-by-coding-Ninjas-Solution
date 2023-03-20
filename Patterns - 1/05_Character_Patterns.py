#Print the following pattern for the given N number of rows.
#Pattern for N = 4
# A
# BC
# CDE
# DEFG

n=int(input())
currRow=1
while currRow<=n:
    currCol=1
    char=ord('A')+currRow-1
    while currCol<=currRow:
        print(chr(char+currCol-1),end="")
        currCol+=1
    print()
    currRow+=1