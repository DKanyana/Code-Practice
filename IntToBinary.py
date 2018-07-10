"""

Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

"""

def add_binary(a,b):
    add = a+b
    result = ""
    while add > 0:
        remainder =add%2
        add = add//2
        result += str(remainder)
    return result[::-1]

#OR 

def add_binary(a,b):
    return bin(a+b)[2:]
        
