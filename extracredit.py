###extracredit assignment###

from graphics import *
import time

'''
cirlces
window
set of functions
time
global
loop
input
if statement
'''

#while True:
# print ('HI')
# time.sleep(1)

wHeight = 1000
wWidth = 1000

win = GraphWin ("My Game", wWidth, wHeight) 


tCirlces = list()

found = 0
clicks = 0

def check(p):
    global tCircles
    for tp in tCircles:
        cx = tp[0]
        cy = tp[1]
        ux = p.getX()
        uy = p.getY()
        if abs(cx - ux) <= 100 and abs(cy - uy) <= 100:
            tCircles.remove(tp)
            return(True, tp)
        return False, None 
        

def main():
    cir_ran_num = int(input("how many random cirlces do you want to find?"))
    print(cir_ran_num)
    #create n number of cirlce
    global wHeight, wWidth
    for i in list(range(cir_ran_num)):
        x = random.randrange(100,wHeight/2)
        y = random.randrange(100, wWidth/2)
        tCirlces.append((x,y))
        if x in tCircles:
            tCircles.append(x)
        if y in tCircles:
            tCircles.append(y)
    print(tCircles) 
                             
    while True:
        userPoint = win.getMouse()
        status, tp = check(userPoint)
        print(userPoint)
        print(status)
        print(tp)
        clicks = clicks + 1
        if status:
            circle = Circle(Point(tp[0], tp[1]), 50)
            circle.setFill("purple")
            circle.draw(win)
            found = found + 1
        print(tCircles)
        if len(tCircles) == 0:
            print("game over clicks {} Founds: {}".format(clicks, found))
            break
    win.close()

main()
                    
                       



main()
