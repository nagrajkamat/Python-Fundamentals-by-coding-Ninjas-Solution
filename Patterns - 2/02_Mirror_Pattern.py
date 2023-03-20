# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# ...1
# ..12
# .123
# 1234
# The dots represent spaces.

n=int(input())
currRow=1
while currRow<=n:
  currCol=1
  spaces=1
  while spaces<=n-currRow:
    print(" ",end="")
    spaces+=1
  while currCol<=currRow:
    print(currCol,end="")
    currCol+=1
    print()
    currRow+=1