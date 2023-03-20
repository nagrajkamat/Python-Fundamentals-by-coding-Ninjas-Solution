# Given a string, determine if it is a palindrome, considering only alphanumeric characters
# Example: If the input string happens to be, "malayalam" then as we see that this word can be read the same as forward and backwards,
# it is said to be a valid palindrome.

#The expected output for this example will print, 'true'.
#From that being said, you are required to return a boolean value from the function that has been asked to implement


s=input()
p=s[::-1]
if(s==p):
    print("true")
else:
    print("false")