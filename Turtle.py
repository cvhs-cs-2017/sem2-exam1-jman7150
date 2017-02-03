"""Create a Turtle Program that will draw a 3-dimensional cube"""
import turtle
exam = turtle.Turtle()

def draw3D(exam):
    for i in range(4):
        exam.forward(150)
        exam.right(90)
    exam.left(150)
    exam.forward(150)
    exam.right(150)
    exam.forward(150)
    exam.right(30)
    exam.forward(150)
    exam.penup()
    exam.goto(0,-150)
    exam.pendown()
    exam.left(180)
    exam.forward(150)
    exam.right(60)
    exam.forward(150)
    
draw3D(exam)
input()

"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""
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
