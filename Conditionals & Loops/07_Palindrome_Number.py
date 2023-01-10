#Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
#Note - Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121


#Code1 -
def checkPalindrome(num):
#Implement Your Code Here
	pass
		
num = int(input())
real_num=num
test_num = 0
while (num > 0):
    remainder = num % 10 
    test_num = (test_num * 10) + remainder
    num = num // 10
if int(test_num)==real_num:    
	print("true")
else:
	print("false")

#Code2 - 
num= int(input())
temp = num
rev=0

while temp != 0:
  rev= (rev 10) + (temp % 10)
  temp = temp // 10

if (num == rev):
  print('true')

else:
  print('false')

