#Nth term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -
    #F(n) = F(n-1) + F(n-2), 
    #Where, F(1) =  1, F(2) = 1
#Provided N you have to find out the Nth Fibonacci Number

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
a = 0
b = 1
i = 1
while i <=n :
    c = a + b
    a = b
    b = c
    i = i + 1
print(a)


#Code2 -
n= int(input())

a = 0
b = 1
c = -1

for i in range(n):
  c=a+b
  a = b
  b = c
print(a)









#Input 1 -
6
#output 1 -
8
#Explanation of Sample Input 1:
#Now the number is ‘6’ so we have to find the “6th” Fibonacci number, So by using the property of the Fibonacci series i.e -
#[ 1, 1, 2, 3, 5, 8, 13, 21]
#So the “6th” element is “8” hence we get the output.