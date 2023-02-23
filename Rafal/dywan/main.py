import turtle
def s(n, bok):
   if n == 0:

       turtle.color('black')

       turtle.begin_fill()
       for _ in range (4):
           turtle.forward(bok)
           turtle.left(90)
       turtle.end_fill()
   else:
       for _ in range(4):
           s(n-1, bok/3)
           turtle.forward(bok/3)
           s(n-1, bok/3)
           turtle.forward(bok/3)
           turtle.forward(bok/3)
           turtle.left(90)
       #turtle.update();
turtle.tracer(100)
s(4, 250)
turtle.done()

turtle.exitonclick()