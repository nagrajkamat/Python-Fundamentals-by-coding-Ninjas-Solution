#Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
#Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.


num = int(input())
test_num = 0
while (num > 0):
    remainder = num % 10
    test_num = (test_num * 10) + remainder
    num = num // 10
    
print(test_num)
#Input 1 -
1234

#Output 1 -
4321