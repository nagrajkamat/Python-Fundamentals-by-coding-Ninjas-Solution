#Write a program to do basic string compression. For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.
#Example:
#If a string has 'x' repeated 5 times, replace this "xxxxx" with "x5".
#The string is compressed only when the repeated character count is more than 1.

from sys import stdin
def getCompressedString(string) :
	# Write your code here.
    if len(string)==0:
        return string
    new_string=""
    i=0
    while i<len(string):
        char=string[i]
        num=0
        while i<len(string) and char==string[i]:
            i=i+1
            num=num+1
        new_string=new_string+char
        if num>1:
            new_string=new_string+str(num)
    return new_string
	

# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)
