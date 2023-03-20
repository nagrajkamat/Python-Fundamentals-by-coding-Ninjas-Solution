#For a given a string(str), find and return the highest occurring character.
#Example:
#Input String: "abcdeapapqarr"
#Expected Output: 'a'
#Since 'a' has appeared four times in the string which happens to be the highest frequency character, the answer would be 'a'.
#If there are two characters in the input string with the same frequency, return the character which comes first.

from sys import stdin
def highestOccuringChar(string):
    n = len(string)
    frequency = [0] * 256
    maxfrequency = 0
    
    for i in range(n) :
        frequency[ord(string[i])] +=1
        maxfrequency = max(maxfrequency, frequency[ord(string[i])])
        
    answer = '\0'
    
    for i in range (n):
        if frequency[ord(string[i])] == maxfrequency :
            answer = string[i]
            break
            
    return answer        

string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)