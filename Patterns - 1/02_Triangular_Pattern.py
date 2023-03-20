#Print the following pattern for the given N number of rows.
#Pattern for N = 4
# *
# **
# ***
# ****

# Approach - 1 
n = int(input())
i = 1
while i <= n :
    j = 1
    p = i
    while j<= i :
        print("*", end="")
        j = j + 1
        p = p + 1
    print()
    i = i + 1
    

# Approach - 2
n=int(input())
for i in range(0, n):
    for j in range(0, i+1):
        print("*",end="")
    print() 

#Ouptut -
# *
# **
# ***
# ****
# *****    