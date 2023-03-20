#Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.
#An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.
#For example,
# 371, as 3^3 + 7^3 + 1^3 = 371
# 1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634

n=int(input())
count=0
orgn=n
orginalno=n
Arms=0
while n>0:
    count+=1
    n=n//10
while orgn>0:
    temp = orgn % 10
    Arms  = Arms  + ((temp)**(count))
    orgn = (orgn //10)
if orginalno==Arms:
    print("true")
else:
    print("false")
