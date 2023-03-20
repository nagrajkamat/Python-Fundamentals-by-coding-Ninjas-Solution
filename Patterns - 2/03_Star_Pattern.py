# Print the following pattern
# Pattern for N = 4
#.....*
#....* *
#...* * *
#..* * * *
#.* * * * *

#The dots represent spaces.
n=int(input())
currRow=1
while currRow<=n:
  spaces=1
  while spaces<=n-currRow:
    print(" ",end="")
    spaces+=1
    currCol=1
  while currCol<=(2*currRow)-1:
    print("*",end="")
    currCol+=1
    print()
    currRow+=1
