#Check Permutation
#Given two strings, S and T, check if they are permutations of each other. Return true or false.
#Permutation means - length of both the strings should same and should contain same set of characters. Order of characters doesn't matter.
#Note : Input strings contain only lowercase english alphabets.


#Input format :
#Line 1 : String 1
#Line 2 : String 2
#Output format :
#'true' or 'false'
#Constraints :
#0 <= |S| <= 10^7
#0 <= |T| <= 10^7
#where |S| represents the length of string, S.
#Sample Input 1 :
#abcde
#baedc
#Sample Output 1 :
#true


def arePermutation(str1, str2):
  n1 = len(str1) 
  n2 = len(str2)
  if (n1 != n2):
    return False
  # Sort both strings 
  a = sorted(str1) 
  str1 = "".join(a) 
  b = sorted(str2) 
  str2 = "".join(b) 
  
  # Compare sorted strings 
  for i in range(0, n1, 1): 
    if (str1[i] != str2[i]): 
      return False
  
    return True
  
str1 = input()
str2 = input()
if (arePermutation(str1, str2)):
    print("true") 
else: 
    print("false") 