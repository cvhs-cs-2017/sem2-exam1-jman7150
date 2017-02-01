"""Create a Turtle Program that will draw a 3-dimensional cube"""




"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""

def DrawRectangle(exam, l, w):
    for i in range (4):
        l = 14
        w = 20
        exam.forward(l)
        exam.right(90)
        exam.forward(w)
DrawRectangle(exam, l , w)
