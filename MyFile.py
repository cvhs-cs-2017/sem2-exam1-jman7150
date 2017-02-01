import turtle
exam = turtle.Turtle()
l = 14
w = 20
n = 8
def AddTen(n):
    n = n + 10
    return n
print (AddTen(10))

"""
def DrawRectangle(exam, l, w):
    for i in range (4):
        l = 14
        w = 20
        exam.forward(l)
        exam.right(90)
        exam.forward(w)
DrawRectangle(exam, l , w)
"""

def DrawPoly(exam, n):
    for i in range (12):

        exam.forward(34)
        exam.right(30)



DrawPoly (exam,8)
input()
