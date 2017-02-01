"""
Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""

def NoVowels(AnyString):
    newString = ""
    for ch in AnyString:
        if ord(ch) is 97 or ord(ch) is 65:
            newString = newString + ""
        elif ord(ch) is 69 or ord(ch) is 101:
            newString = newString + ""
        elif ord(ch) is 73 or ord(ch) is 105:
            newString = newString + ""
        elif ord(ch) is 79 or ord(ch) is 111:
            newString = newString + ""
        elif ord(ch) is 85 or ord(ch) is 117:
            newString = newString + ""


        else:
            newString = newString + ch
    return newString
String = "Computer Science Makes the World go round but it doesn't make the world round itself!"

x = NoVowels(String)
print (x)





"""Write an encryption code that you make up and run it for the variable NoVowels"""
def NoVowels(x):
    newString = ""
    for ch in x:
        if ord(ch) is 97 or ord(ch) is 65:
            newString = newString + "$"
        elif ord(ch) is 69 or ord(ch) is 101:
            newString = newString + "^"
        elif ord(ch) is 73 or ord(ch) is 105:
            newString = newString + "*"
        elif ord(ch) is 79 or ord(ch) is 111:
            newString = newString + "%"
        elif ord(ch) is 85 or ord(ch) is 117:
            newString = newString + "!"


        else:
            newString = newString + ch
    return newString
String = "Computer Science Makes the World go round but it doesn't make the world round itself!"

x = NoVowels(String)
print (x)
