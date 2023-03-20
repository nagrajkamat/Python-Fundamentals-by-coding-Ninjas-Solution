n=int(input())
i=1
while(i<=n):
  j=1
  while(j<=n-i):
    print(" ",end='')
    j+=1
    k=1
  while(k<=i):
    print(i-k+1,end='')
    k+=1
    p=2
  while(p<=i):
    print(p,end='')
    p+=1
    print()
    i+=1

# Output -
#    1
#   212
#  32123
# 4321234