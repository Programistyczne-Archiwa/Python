import turtle
import random
import math

zolw = turtle.Turtle()
zolw.shape("turtle")
zolw.color("green")
zolw.speed(20)

# def triangle(bok, fill = False):
#     if fill == True:
#         turtle.begin_fill()
#     for i in range(3):
#         turtle.left(120)
#         turtle.forward(bok)
#     if fill == True:
#         turtle.end_fill()

# def treeiangle(bok):
#     positions = []
#     triangle(bok)
#     positions.append(turtle.pos())
#     triangle(bok/2)
#     turtle.left(120)
#     turtle.forward(bok/2)
#     turtle.setheading(0)
#     positions.append(turtle.pos())
#     triangle(bok/2)
#     turtle.right(120)
#     turtle.forward(bok/2)
#     turtle.setheading(0)
#     positions.append(turtle.pos())
#     triangle(bok/2)
#     return positions

# def main(start_positions = [], bok = 200):
#     new_positions = []
#     print(start_positions)
#     for i in start_positions:
#         turtle.penup()
#         print(i)
#         turtle.setpos(i)
#         turtle.pendown()
#         new_positions += treeiangle(bok)
#     main(new_positions, bok/2)

# main(start_positions=[(0, 0)])

# def triangle(bok):
#     data = {
#         "positions": [],
#         "rotations": []
#     }
#     turtle.left(60)
#     turtle.forward(bok/3)
#     turtle.penup()
#     data["positions"].append(turtle.pos())
#     data["rotations"].append(turtle.heading())
#     turtle.forward(bok/3)
#     turtle.pendown()
#     turtle.forward(bok/3)
#     turtle.right(120)
#     turtle.forward(bok/3)
#     turtle.penup()
#     data["positions"].append(turtle.pos())
#     data["rotations"].append(turtle.heading())
#     turtle.forward(bok/3)
#     turtle.pendown()
#     turtle.forward(bok/3)
#     return(data)

# def draw_triangle(start_positions, start_rotations, bok):
#     new_positions = []
#     new_rotations = []
#     print(start_positions)
#     print(start_rotations)
#     for i in range(len(start_positions)):
#         turtle.penup()
#         print(i)
#         turtle.setpos(start_positions[i])
#         turtle.setheading(start_rotations[i])
#         turtle.pendown()
#         data = triangle(bok)
#         new_positions += data["positions"]
#         new_rotations += data["rotations"]
#     return draw_triangle(new_positions, new_rotations, bok/2)


# bok = 200
# data = triangle(bok)
# draw_triangle(data["positions"], data["rotations"], bok/2)


# turtle.exitonclick()

turtle.speed(10)


def triangle(bok):
    data = {"positions": [], "rotations": []}
    for i in range(3):
        data["positions"].append(turtle.pos())
        data["rotations"].append(turtle.heading())
        turtle.forward(bok)
        turtle.left(120)
    return data


def draw_triangles(data, bok):
    new_data = {"positions": [], "rotations": []}
    for i in range(len(data["positions"])):
        turtle.penup()
        turtle.setpos(data["positions"][i])
        turtle.setheading(data["rotations"][i])
        turtle.right(60)
        turtle.pendown()
        temp_data = triangle(bok)
        new_data["positions"] += temp_data["positions"]
        new_data["rotations"] += temp_data["rotations"]
    draw_triangles(new_data, bok / 2)


data = triangle(200)
draw_triangles(data, 200 / 2)

turtle.exitonclick()
