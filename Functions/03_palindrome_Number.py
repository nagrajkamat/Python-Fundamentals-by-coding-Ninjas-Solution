#Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
#Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121

def checkPalindrome(n):
    x = n
    rev = 0
    while x > 0:
        a = x % 10
        rev = rev * 10 + a
        x = x // 10
    if n == rev:
        return True
    else:
        return False
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
