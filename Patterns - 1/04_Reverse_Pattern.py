N = 4

n = int(input())
i = 1
while i <= n :
    j = 1
    k = i
    while j <= i :
        print( k, end= "" )
        j = j + 1
        k = k - 1
    print()
    i = i + 1

# Output -
# 1    
# 21
# 321
# 4321