from Myro import *
init("sim")
def CircleyCircle(x):
    penDown()
    move(.5,1)
    wait(x)
    stop()
    penUp()
def swayIntro(y):
    while y > 0:
        turnLeft(6,.5)
        turnRight(6,.5)
        y=y-1
CircleyCircle(6)
forward(1,1.1)
swayIntro(6)
turnRight(4,1)

