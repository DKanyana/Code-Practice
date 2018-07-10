===================
Problem -
Take 2 strings s1 and s2 including only letters from ato z. 
Return a new sorted string, the longest possible, containing distinct letters.
===================

Solution - 
def longest(s1, s2):
    combineStr = s1+s2 #Combine strings s1 and s2
    longestStr = set(combineStr) #Create a set from the combined string
    return ''.join(sorted(longestStr)) #Sort the set and join it to form a string
    
 def longest(s1, s2):
    combineStr = s1+s2 #Combine strings s1 and s2
    uniqueStr = '' #initialize a new string
    alphabet = 'abcdefghijklmnopqrstuvwxyz' #Define a string containing all the alphabets
    
    for char in alphabet: #Loop through the alphabet list
        if char in combineStr: #Check if the character in the alphabet list is present in the combined string
            uniqueStr +=char #If present, append concatenate it to the new string
    return uniqueStr
