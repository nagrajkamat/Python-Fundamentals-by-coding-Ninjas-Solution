#For a given string(str), remove all the consecutive duplicate characters.
#Example:
#Input String: "aaaa"
#Expected Output: "a"

#Input String: "aabbbcc"
#Expected Output: "abc"

import itertools
def remove_consecutive_duplicates(s1):
     return (''.join(i for i, _ in itertools.groupby(s1)))

s1= input()
print(remove_consecutive_duplicates(s1))
