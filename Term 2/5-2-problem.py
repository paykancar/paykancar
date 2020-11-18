import turtle as tr
import random as rnd



for j in range(100):
    tr.penup()
    x_position = rnd.randint(-400, 300)
    y_position = rnd.randint(-600, 200)
    tr.goto(x_position, y_position)
    tr.pendown()
    pen_size = rnd.randint(1, 4)
    tr.pensize(pen_size)
    tr.speed(10000)
    for i in range(4):
        tr.fd(300)
        tr.lt(90)


tr.done()