#For a given a string(str) and a character X, write a function to remove all the occurrences of X from the given string.
#The input string will remain unchanged if the given character(X) doesn't exist in the input string.

from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
    length = len(string)
    str2 = ""
    for i in range(length):
        if string[i]!=ch:
            str2 += string[i]
    return str2    


#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)