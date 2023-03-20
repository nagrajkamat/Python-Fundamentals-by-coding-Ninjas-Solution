#Print the following pattern for the given number of rows.
#Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE

n = int(input())
i = 1
while i <= n:
    j = 1
    s_c = chr(ord('A')+n-i)
    while j <= i:
        c_p = chr(ord(s_c)+j-1)
        print(c_p,end='')
        j = j+1
    print()
    i= i+1