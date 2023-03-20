#Print the following pattern for the given number of rows.
#Pattern for N = 4
#4444444
#4333334
#4322234
#4321234
#4322234
#4333334  
#4444444

n=int(input())
pattern_1=n

for i in range (1,n+1):
    pattern_3 = n
    for k in range(1,i):
        print(pattern_3,end="")
        pattern_3-=1
    for j in range (1,2*n+2-2*i):
        print(pattern_1,end="")
    pattern_1 -= 1

    for l in range (1,i):
        pattern_3+=1
        print(pattern_3,end="")
    print("")
pattern_1=2

for i in range (n,1,-1):
    pattern_3 = n
    for k in range(1,i):
        print(pattern_3,end="")
        pattern_3-=1
    for j in range (1,2*n+2-2*i):
        print(pattern_1,end="")
    pattern_1+= 1

    for l in range (1,i):
        pattern_3+=1
        print(pattern_3,end="")
    print("")