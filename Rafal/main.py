import random
import turtle
t = turtle.Turtle()
def tutel():
    t.begin_fill()
    t.left(90)
    t.color('red')
    t.pensize(10)
    t.forward(200)
    t.color('blue')
    t.left(90)
    t.forward(200)
    t.end_fill()

def sixangle():
    i = 0

    t.begin_fill()
    for i in range(0,6):
        t.forward(80)
        t.left(60)
    t.color("teal")
    t.end_fill()


def kwadrats():


    for i in range(50,3000,2):
        t.bgcolor("black")

        t.color(random.choice(['white', 'yellow', 'red', 'orange', 'blue']))
        t.forward(i)
        t.right(91)
def triangle(deg, len):
    t.left(deg)
    t.forward(len)
    for i in range(0,3):
        t.forward(100)
        t.left(120)
def trojkats():
    t.speed(1)
    triangle(120,0)
    triangle(120,0)

    triangle(300,50)

def codosiura(bok, n):
    if n==0:
        t.forward(bok)
        return
    codosiura(bok/3,n-1)
    t.left(60)
    codosiura(bok / 3, n - 1)
    t.right(120)
    codosiura(bok / 3, n - 1)
    t.left(60)
    codosiura(bok / 3, n - 1)

#    t.forward(bok)
#    t.left(30)
#    drzewo(bok/2,n-1)
#    t.right(60)
#    drzewo(bok/2,n-1)
#    t.left(30)

def drzewo(bok, n):
    t.forward(bok)
    if n==0:

        return
    t.left(30)
    position = t.pos()
    t.forward(bok)
    position2 = t.pos()
    t.up()
    t.setpos(position)
    t.down()
    t.right(60)
    t.forward(bok)
    t.left(60)
    t.up()
    t.setpos(position2)
    t.down()
    drzewo(bok/3,n-1)

def dywan(n, bok):
   if n == 0:
       t.color('black')
       t.begin_fill()
       for _ in range (4):
           t.forward(bok)
           t.left(90)
       t.end_fill()
   else:
       for _ in range(4):
           dywan(n-1, bok/3)
           t.forward(bok/3)
           dywan(n-1, bok/3)
           t.forward(bok/3)
           t.forward(bok/3)
           t.left(90)
       #turtle.update();



def trojkaty(bok, n):
        if n==0:
            for _ in range(3):
                t.forward(bok)
                t.left(120)
        else:
            trojkaty(bok/2,n-1)
            t.left(60)
#            t.forward(bok/4)
            trojkaty(bok/4,n-1)
            t.forward(bok/2)
            t.right(120)
            trojkaty(bok/4,n-1)
            t.forward(bok/2)
            t.right(120)
            trojkaty(bok/4,n-1)
t.speed(2)

# t.tracer(100)

trojkaty(200,1)


# dywan(5, 400)
# drzewo(100,4)
# codosiura(400,10)
# trojkats()
# sixangle()
# kwadrats()
turtle.exitonclick()

