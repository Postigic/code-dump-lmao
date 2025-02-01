import turtle


def koch(t, length):
    if length < 25:
        t.fd(length)
        return
    segment = length / 3
    koch(t, segment)
    t.lt(60)
    koch(t, segment)
    t.rt(120)
    koch(t, segment)
    t.lt(60)
    koch(t, segment)


def snowflake(t, length):
    for _ in range(3):
        koch(t, length)
        t.rt(120)


turt = turtle.Turtle()
turt.speed(0)
turt.pu()
turt.goto(-150, 0)
turt.pd()

snowflake(turt, 300)

turtle.done()