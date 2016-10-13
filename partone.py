from Myro import *
init("sim")
def CircleyCircle(x):
    penDown()
    move(.5,1)
    wait(x)
    stop()
    penUp()
def swayRhythm(x):
    for i in range(0,x):
        turnLeft(5,.42)
        stop()
        turnRight(5,.42)
        stop()
def sharpTurn(x):
    for i in range(0,x):
        turnRight(9,.2)
        wait(.4)
def slide(x):
    forward(2,x)
    stop()
def back(x):
    backward(2,x)
    stop()
def TaeVerseEnd(x):
    for i in range (0,x):
        slide(.42)
CircleyCircle(6)
forward(1,1.1)
swayRhythm(6)
turnRight(4,2.2)
swayRhythm(6)
sharpTurn(3)
wait(.1)
slide(.8)
back(.8)
TaeVerseEnd(2)
CircleyCircle(4)
back(2)
slide(1)
sharpTurn(8)
CircleyCircle(5)




