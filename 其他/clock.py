from turtle import *
import time


def week():
    return time.strftime('%A')


def date():
    a = time.strftime('%d %m %Y %H:%M:%S')
    return a


def set_shape(name, length):
    reset()
    begin_poly()
    forward(length)
    end_poly()
    er = get_poly()
    register_shape(name, er)


def Init():
    global secHand, minHand, hurHand, printer
    mode("logo")  # 重置turtle指向北

    set_shape("secHand", 125)  # 建立三个表针并初始化
    set_shape("minHand", 130)
    set_shape("hurHand", 90)

    secHand = Turtle()
    secHand.shape("secHand")
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)


def Tick():
    second = int(time.strftime('%S'))
    minute = int(time.strftime('%M')) + second / 60.0
    hour = int(time.strftime('%H')) + minute / 60.0
    secHand.setheading(6 * second)
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)
    ontimer(Tick, 100)


def clock():
    speed(100)
    m = 1
    for x in range(1, 61):
        penup()
        home()
        right(6 * x)
        if x % 5 != 0:
            forward(200)
            pendown()
            pensize(6)
            forward(10)
        else:
            forward(200)
            pendown()
            pensize(6)
            forward(20)
            penup()
            forward(20)
            write(str(m), align="center")
            m += 1
    hideturtle()
    home()


def writer():
    pensize(10)
    forward(0)
    penup()
    forward(150)
    pendown()
    write(week(), align="center")
    penup()
    backward(200)
    pendown()


def main():
    hideturtle()
    Init()
    hideturtle()
    reset()
    Tick()
    clock()
    writer()


if __name__ == "__main__":
    main()
    penup()
    backward(50)
    pendown()
    while True:
        write(date(), align="center")
        time.sleep(0.9)
        undo()
