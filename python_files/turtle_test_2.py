import turtle as tur
from random import randint

tur.title('Welcome to Rainbow Road!')

tur.speed(10)
tur.bgcolor('black')

x = 1
while x < 400:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tur.colormode(255)
    tur.pencolor(r, g, b)

    tur.fd(50 + x)
    tur.rt(90.911)

    x += 1

tur.exitonclick()
