#Imports
import pygame as pyg
import sys

pyg.init()

#Globals
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 300
SCREEN = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pyg.font.Font("freesansbold.ttf", 20)

def fun0(a,b,c,d):
    return (a and not b and not c) or (not a and c) or (not b and not c and not d) or (not a and b and d)
def fun1(a,b,c,d):
    return (not a and b and not c) or (not a and b and not d) or (a and not b and not c) or (not a and not c and not d)
def fun2(a,b,c,d):
    return (not a and not b) or (not b and not c) or (not a and not c and not d) or (not a and c and d)
def fun3(a,b,c,d):
    return (a and not b and not c) or (not a and b and not c) or (not a and not b and c) or (not a and c and not d)
def fun4(a,b,c,d):
    return (not a and c and not d) or (not b and not c and not d)
def fun5(a,b,c,d):
    return a or b or not c or d
def fun6(a,b,c,d):
    return a or (c and not d) or (not a and not b and c) or (b and not c and d) or (not b and not c and not d)

#Main
def main():
    clock = pyg.time.Clock()

    dashes = [pyg.Rect(100,50,100,20),
              pyg.Rect(80,70,20,100),pyg.Rect(200,70,20,100),
              pyg.Rect(100,170,100,20),
              pyg.Rect(80,190,20,100),pyg.Rect(200,190,20,100),
              pyg.Rect(100,290,100,20)]
    
    on = [False for i in range(7)]

    x=0
    #MAIN LOOP
    run = True
    while run:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                sys.exit()
            elif event.type == pyg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if x<9:
                        x+=1
                    else:
                        x=0
                elif event.button == 3:
                    if x>0:
                        x-=1
                    else:
                        x=9

        SCREEN.fill((30, 30, 30))

        xt=x
        xa = [0,0,0,0]
        for j in range(4):
            if xt % 2 == 1:
                xa[j] = 1
                xt -= 1
            xt /= 2
        xa.reverse()
        a,b,c,d=xa

        for i in range(7):
            exec(f"on[{i}]=fun{i}(a,b,c,d)")

        for i,dash in enumerate(dashes):
            if on[i]:
                pyg.draw.rect(SCREEN,(220,220,220),dash)
            else:
                pyg.draw.rect(SCREEN,(10,10,10),dash)

        pyg.display.set_caption(f'7 Segment Display--{int(clock.get_fps())}')
        clock.tick(30)
        pyg.display.update()

main()