import turtle as tur

tur.title('First turtle')

tur.speed(10)
tur.bgcolor('black')
tur.pencolor('blue')

tur.up()

tur.rt(45)
tur.fd(90)
tur.rt(135)

tur.down()

x = 0
while x < 120:
    i = 0
    while i < 6:
        tur.fd(200), tur.rt(61)
        i += 1
    tur.rt(11.1111)
    x += 1

tur.exitonclick()
