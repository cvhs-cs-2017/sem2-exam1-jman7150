"""Use the range function to print the numbers from 40 to 1 (backwards)"""
for i in range(40,0,-1):
    print (i)


"""Repeat the exercise but count by 5's"""
for i in range(40,-1,-5):
    print (i)


"""Write a program that will count print all the multiples of (n) where n is
taken from user input.  Include necessary print statements."""
print("Choose any number.")
n = int(input())
for i in range(n, 12):
    n = n + 10
    print(n)

#12 is used to achieve the ten multiples of 10 after 2
