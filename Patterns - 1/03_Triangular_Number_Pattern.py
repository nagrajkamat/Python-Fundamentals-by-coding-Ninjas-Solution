#Print the following pattern for the given N number of rows.
#Pattern for N = 4
# 1
# 22
# 333
# 4444


# Approach - 1 
n = int(input())
i = 1
p = 1
while i <= n :
    j = 1
    while j <= i :
        print(i , end="")
        j = j + 1
    print()
    i = i + 1