#Print the following pattern for the given number of rows.
#Pattern for N = 5
# 1    2   3    4   5
# 11   12  13   14  15
# 21   22  23   24  25
# 16   17  18   19  20
# 6    7    8   9   10

n=int(input())
startvalue=1
for i in range(1,n+1):
    for j in range(startvalue,startvalue+n):
        print(j,end=" ")
    print()
    if i==(n+1)//2:
        if n%2!=0:
            startvalue=n*(n-2)+1
        else:
            startvalue=n*(n-1)+1
    elif i>(n+1)//2:
        startvalue=startvalue-2*n
    else:
        startvalue=startvalue+2*n