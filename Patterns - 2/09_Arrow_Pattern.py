#Print the following pattern for the given number of rows.
#Assume N is always odd.
#Note : There is space after every star.
#Pattern for N = 7
# *
#  * *
#    * * *
#      * * * *
#    * * *
#  * *
# *

n = int(input())
i = 1
n1 = (n - 1) / 2
n = (n + 1) / 2
while i <= n:
    spaces = 2
    while spaces <= i:
        print(" ", end="")
        spaces += 1
    star = 1
    while star <= i:
        print("* ", end="")
        star += 1
    print("")
    i = i + 1

i = 1
g = 0
while i <= n1:
  num_1 = n1 - 1
  while num_1 >= i:
    print(" ", end="")
    num_1 -= 1

    num_1 = n1 - 1
  while num_1 >= g:
    print("* ", end="")
    num_1 -= 1
    print()
    i = i + 1
    g = g + 1