import turtle
from math import sin, cos, radians

def draw_clock_face(t):
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.circle(250)

    for i in range(12):
        angle = radians(i * 30)
        x_inner = 200 * sin(angle)
        y_inner = 200 * cos(angle)
        x_outer = 230 * sin(angle)
        y_outer = 230 * cos(angle)
        t.penup()
        t.goto(x_inner, y_inner)
        t.pendown()
        t.goto(x_outer, y_outer)
