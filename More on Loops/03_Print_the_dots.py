#Print the following pattern for the given number of rows.
#Note: N is always odd. n = 5
#       *
#      * *
#     * * *
#      * *
#       *
#The gap between represent spaces.

n=int(input())
x = (n//2)+1
y = (n//2)
for i in range(1,x+1):
    for j in range(x-i):
        print(" ",end="")
    for l in range(2*i-1):
        print("*",end="")
    print()
for a in range(y,0,-1):
    for s in range(y-a+1):
        print(" ",end="")
    for k in range(2*a-1):
        print("*",end="")
    print()