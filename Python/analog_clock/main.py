import turtle
import time
from clock_face import draw_clock_face
from clock_hands import create_hand, draw_hand

screen = turtle.Screen()
screen.title("Analog Clock")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

clock = turtle.Turtle()
clock.hideturtle()
clock.pensize(3)
clock.color("white")
draw_clock_face(clock)

second_hand = create_hand("red", 1)
minute_hand = create_hand("blue", 3)
hour_hand = create_hand("green", 5)

while True:
    now = time.localtime()
    sec = now.tm_sec
    minute = now.tm_min
    hour = now.tm_hour % 12

    sec_angle = sec * 6
    min_angle = minute * 6 + sec * 0.1
    hour_angle = hour * 30 + minute * 0.5

    draw_hand(second_hand, 180, sec_angle)
    draw_hand(minute_hand, 150, min_angle)
    draw_hand(hour_hand, 100, hour_angle)

    screen.update()
    time.sleep(1)
