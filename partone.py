from Myro import *
init("sim")
def CircleyCircle(x):
    penDown()
    move(.5,1)
    wait(x)
    stop()
    penUp()
def swayRhythm(x):
    while x > 0:
        turnLeft(5,.42)
        stop()
        turnRight(5,.42)
        stop()
        x=x-1
def sharpTurn(x):
    while x > 0:
        turnRight(9,.2)
        x=x-1
        wait(.35)
def slide(x):
    forward(2,x)
    stop()
def back(x):
    backward(2,x)
    stop()
CircleyCircle(6)
forward(1,1.1)
swayRhythm(6)
turnRight(4,2.2)
swayRhythm(6)
sharpTurn(3)
wait(.2)
slide(1.1)
back(1.1)
slide(.42)
back(.42)
slide(.42)


