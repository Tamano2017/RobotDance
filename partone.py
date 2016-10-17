from Myro import *
from Graphics import *
sim=Simulation("My World", 700, 600, Color("lightBlue"))
makeRobot("SimScribbler",sim)
sim.setup()
def CircleyCircle(x):
    move(.5,-1)
    wait(x)
    stop()
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
        back(.42)
def ChorusLeft(x):
    for i in range (0,x):
        forward(8,.2)
        forward(.5,.1)
        stop()
        wait(.1)
        backward(8,.2)
        backward(.5,.1)
        wait(.2)
def ChorusRight(x):
    for i in range (0,x):
        backward(8,.2)
        backward(.5,.1)
        stop()
        wait(.1)
        forward(8,.2)
        forward(.5,.1)
        stop()
        wait(.2)
penDown() #helps me tell when to start music
CircleyCircle(6)
penUp()
forward(1,1.1)
swayRhythm(6)
turnRight(4,2.2)
swayRhythm(6)
sharpTurn(3)
wait(.1)
slide(.8)
back(.8)
TaeVerseEnd(2)
turnBy(-20)
wait(3)
back(2)
slide(1.4)
sharpTurn(7)
CircleyCircle(6)
wait(1)
sharpTurn(9)
wait(8.5)
ChorusLeft(4)
wait(.2)
ChorusRight(2)
sharpTurn(1)
wait(1.2)
ChorusLeft(4)
wait(1)
sharpTurn(3)







