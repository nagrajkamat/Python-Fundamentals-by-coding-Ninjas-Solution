
#Aadil has been provided with a sentence in the form of a string as a function parameter. The task is to implement a function so as to print the sentence such that each word in the sentence is reversed.
#Example:
#Input Sentence: "Hello, I am Aadil!"
#The expected output will print, ",olleH I ma !lidaA".

from sys import stdin


def reverseEachWord(string) :
	# Your code goes here
    if len(string) is 0:
        return string
    words=string.split(" ")
    new_str=""
    for word in words:
        new_word=word[::-1]
        new_str+=new_word+" "
    return new_str


#main
string = stdin.readline().strip()
ans = reverseEachWord(string)
print(ans)