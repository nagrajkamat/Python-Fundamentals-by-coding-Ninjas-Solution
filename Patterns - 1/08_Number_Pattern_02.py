# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 11
# 202
# 3003

# Approach 1 -
n = int(input())
i = 1
p = 1
while i <= n :
    if i==1:
        print(i,end="")
    else:
        print(i-1,end="")
        j=1
        while j<=i-2:
            print(0,end="")
            j=j+1
        print(i-1,end="")
    i=i+1
    print()

# Approach 2 -
n=int(input())
print(1)
i=1
while(i<n):
    j=0
    while(j<i+1):
        if(j==0 or j==i):
            print(i,end="")
        else:
            print(0,end="")
        j=j+1
    i=i+1
    print() 