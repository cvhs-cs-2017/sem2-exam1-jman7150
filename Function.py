"""Define a function that will take a parameter, n, and triple it and return
the result"""
def triple(x):
    x = x * 3
    return x
print(triple(12))




"""Write a program that will prompt the user for an input value (n) and print
the result of 3n by calling the function defined above.  Make sure you include
the necessary print statements and address any issues with whitespace. """
print("Input a value")
n = int(input())
print(triple(n))
