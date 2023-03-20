#Print the following pattern for the given N number of rows.
#Pattern for N = 3
# A
# BB
# CCC

n=int(input())
for i in range(65,65 + n):
    for j in range(65,i+1):
        print(chr(i),end='')
    print("")