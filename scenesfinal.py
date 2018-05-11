from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import*
from math import*
import numpy as np


def circle(xr,yr,r,g,b):
    glColor(r, g, b)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, 0.001):
        x = 0.1 * cos(theta)
        y = 0.1 * sin(theta)
        glVertex2d( x+xr , y+yr )
    glEnd()
    
def square(x,y,r,g,b):
    glColor(r,g,b)
    glBegin(GL_POLYGON)
    glVertex2d(x-.5,y+.5)
    glVertex2d(x+.5,y+.5)
    glVertex2d(x+.5,y-.5)
    glVertex2d(x-.5,y-.5)

    glEnd()
    
def triangle(x,y,r,g,b):
    glColor(r, g, b)
    glBegin(GL_POLYGON)
    glVertex2d(x - .5, y + .5)
    glVertex2d(x + .5, y + .5)
    glVertex2d(x , y - .5)
    glEnd()


def drawText(string, x, y):
    glLineWidth(3)
    glColor(.5, 0.5, 1)  # Yellow Color
    glLoadIdentity()
    glTranslate(x, y, 0)
    glScale(0.0009, 0.0009, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

#named S1

def S1() :
    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glTranslate(0,-0.9,0)
    glScale(2,0.3,0)
    square(0,0,0.7,0.7,0.7)    # THE GROUND


    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glTranslate(0,0.95,0)
    glScale(2,0.15,0)
    square(0,0,0.7,0.7,0.7)    # TOP


    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glTranslate(-0.97,0.7,0)
    glScale(0.1,1,0)
    square(0,0,0.7,0.7,0.7)   # left wall

    glLoadIdentity()      #left C thing
    glRotate(180, 0, 1, 0)
    glTranslate(-0.75,0.05,0)
    glScale(0.7,0.6,0)
    glColor(0.7,0.7,0.7)
    glBegin(GL_POLYGON)
    glVertex2d(-0.5,0.3)
    glVertex2d(0.07,0.3)
    glVertex2d(0.07,0.2)
    glVertex2d(-0.25,0.2)
    glVertex2d(-0.25,-0.4)
    glVertex2d(-0.5,-0.5)
    glEnd()
    glColor(0.7, 0.7, 0.7)
    glBegin(GL_POLYGON)
    glVertex2d(-0.3,-0.4)
    glVertex2d(0.25, -0.4)
    glVertex2d(0.25, -0.5)
    glVertex2d(-0.5, -0.5)
    glEnd()


    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glTranslate(0.95, 0.7, 0)
    glScale(0.25, 0.7, 0)
    square(0, 0, 0.7,0.7,0.7)  # Right top wall

    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glTranslate(0.93, -0.7, 0)
    glScale(0.3, 0.7, 0)
    square(0, 0, 0.7,0.7,0.7)  # right down wall

    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glTranslate(0.3,-0.63,0)
    glScale(0.8,1.2,0)
    glColor(0.7,0.7,0.7)
    glBegin(GL_POLYGON)
    glVertex3d(0, 0.07, 0)
    glVertex3d(0, 0.2, 0)
    glVertex3d(0.2, 0.2, 0)
    glVertex3d(0.2, -0.1, 0)
    glVertex3d(-0.3, -0.1, 0)
    glVertex3d(-0.3, 0.07, 0)
    glEnd()
    #        # LADDER


    glLoadIdentity()    # elbta3 elly f elhwa :"D
    glRotate(180, 0, 1, 0)
    glScale(0.3,0.07,0)
    square(0.7,0,0.7,0.7,0.7)
    #

    glLoadIdentity()  # elbta3 elly f elhwa :"D
    glRotate(180, 0, 1, 0)
    glScale(0.3, 0.07, 0)
    square(-0.4, 2.5, 0.7, 0.7, 0.7)

    glLoadIdentity()
    glTranslate(-0.95,0,0)
    glScale(0.19,0.7,0)
    square(0,0,0.7,0,0)
    drawText("Don't be greedy",-.75,.7)
#named 2ndscene
def S2():
    glClearColor(0.2, 0.2, 0.2, 0)
    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glScale(0.5,0.2,0)
    square(-1.5,-1,0.7,0.7,0.7)  # Left log

    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glTranslate(-0.98,-0.55,0)
    glScale(0.05,0.5,0)
    square(0,0,0.7,0.7,0.7)    #  Left Bottom wall

    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glTranslate(-0.4,-0.9,0)
    glScale(1.3,0.2,0)
    square(0,0,0.7,0.7,0.7) #  left bottom ground


    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glRotate(180,0,0,1)
    glScale(0.1,0.1,0)
    for x in range (-2,10,1):
        triangle(x,7.5,1,1,1)    # the knifes lol


    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glTranslate(0.325,-0.45,0)
    glScale(0.15,1.2,0)
    square(0,0,0.7,0.7,0.7)       # the middle wall


    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glScale(0.5,0.5,0)
    square(-1.5,1.5,0.7,0.7,0.7)   # top left square


    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glScale(0.1,0.4,0)
    square(9.5,2,0.7,0.7,0.7)   # top right corner

    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glScale(0.4,0.3,0)
    square(2,1.5,0.7,0.7,0.7)   # Right LOG :: moving

    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glScale(0.1,0.5,0)
    square(9.5,0.1,0.7,0.7,0.7)   # right wall

    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glTranslate(0.8,-0.9,0)
    glScale(0.75,1,0)
    glColor(0.7,0.7,0.7)
    glBegin(GL_POLYGON)
    glVertex3d(-0.1, 0.07, 0)
    glVertex3d(-0.1, 0.15, 0)
    glVertex3d(0.27, 0.15, 0)
    glVertex3d(0.27, -0.15, 0)
    glVertex3d(-0.54, -0.15, 0)
    glVertex3d(-0.54, 0.07, 0)
    glEnd()            # right bottom corner


    glLoadIdentity()
    glScale(1.4,0.1,0)
    square(-0.143,9.5,0.7,0.7,0.7) #  Top
    drawText("Other controllers",-.7,.7)


def S3():
    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glScale(1.25,0.8,0)
    glTranslate(-0.08,-0.4,0)
    square(-0.4,-0.4,0.7,0.7,0.7)   # ground chunk


    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glRotate(180,0,0,1)
    glScale(0.1,0.1,0)
    for x in range (-9,0,1):
        triangle(x,7.5,1,1,1)    # the knifes lol


    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glScale(1.2,0.2,0)
    glTranslate(0.15,-2.25,0)
    square(0.15,-2.25,0.7,0.7,0.7)   # under the knives

    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glScale(1.5,0.3,0)
    glTranslate(0.25,-0.83,0)
    square(0.5,0,0.7,0.7,0.7) #### Moving part


    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glScale(0.1,0.85,0)
    glTranslate(5,-0.34,0)
    square(5,-0.34,0.7,0.7,0.7)   #down right under the moving part fakss

    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glScale(0.5,0.5,0)
    glTranslate(0.75,0.75,0)
    square(0.75,0.75,0.7,0.7,0.7)

    glLoadIdentity()
    glScale(0.1,0.6,0)
    square(1.2,0.1,0.7,0.2,1) # DOOR

    glLoadIdentity()
    glScale(0.1,0.5,0)
    square(1.2,1.2,0.7,0.7,0.7) # over the DOOR

    glLoadIdentity()
    glScale(0.1,1.1,0)
    square(9.5,0.25,0.7,0.7,0.7) # right wall


    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glScale(0.8,0.2,0)
    glTranslate(0.063,2.3,0)
    square(0.063,2.3,0.7,0.7,0.7)   #top

    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glScale(0.3, 0.2, 0)
    glTranslate(-1.5,2.3,0)
    square(-1.5, 2.3, 0.7, 0.7, 0.7)  # top
    drawText("I believe i can ...",-.95,.35)

#Riad
def S4():
    def walls(red, green, blue):
        glRotate(180, 0, 1, 0)
        glColor(red, green, blue)
        glBegin(GL_POLYGON)
        glVertex2d(-0.5, 0.5)
        glVertex2d(0.5, 0.5)
        glVertex2d(0.5, -0.5)
        glVertex2d(-0.5, -0.5)
        glEnd()

    def draw_left_wall():
        glLoadIdentity()
        glTranslate(-1, 0, 0)
        glScale(0.1, 2, 0)
        walls(0.7, 0.7, 0.7)

    def draw_Up_wall():
        glLoadIdentity()
        glRotate(180, 0, 1, 0)
        glTranslate(0.0, 1, 0.0)
        glScale(2, .2, 0.0)
        walls(0.7, 0.7, 0.7)

    def draw_right_wall():
        glLoadIdentity()
        glTranslate(1, 0.5, 0.0)
        glScale(0.1, 1.4, 0.0)
        walls(0.7, 0.7, 0.7)

    def draw_gound():
        part_1()
        part_2()
        part_3()
        part_4()
        part_5()

    def part_1():
        glLoadIdentity()
        glRotate(180, 0, 1, 0)
        glScale(0.6, 0.25, 0.0)  # shape
        glTranslate(1.19, -3.5, 0.0)  # Position
        walls(0.7, 0.7, 0.7)  # the fabric to draw with :D

    def part_2():
        glLoadIdentity()
        glRotate(180, 0, 1, 0)
        glScale(0.30, 0.60, 0.0)
        glTranslate(0.88, -1.5, 0)
        walls(0.7, 0.7, 0.7)

    def part_3():
        glLoadIdentity()
        glRotate(180, 0, 1, 0)
        glScale(0.4, 0.25, 0.0)
        glTranslate(-0.15, -3.5, 0.0)
        walls(0.7, 0.7, 0.7)

    def part_4():
        glLoadIdentity()
        glScale(0.3, 0.5, 0.0)
        glTranslate(3, -1.5, 0.0)
        walls(0.7, 0.7, 0.7)

    def part_5():
        glLoadIdentity()
        glRotate(180, 0, 1, 0)
        glScale(0.4, 0.05, 0.0)
        glTranslate(-1.25, -19.5, 0.0)
        walls(0.7, 0.7, 0.7)

    def UP_side_trap():
        glColor(1, 1, 1)
        glBegin(GL_POLYGON)
        glVertex2d(0.0, 0.1)
        glVertex2d(0.0, 0.2)
        glVertex2d(0.15, 0.2)
        glEnd()

    def down_side_trap():
        glColor(1, 1, 1)
        glBegin(GL_POLYGON)
        glVertex2d(0.0, 0.2)
        glVertex2d(0.0, 0.3)
        glVertex2d(0.15, 0.2)
        glEnd()

    def draw_side_trap_1():
        glLoadIdentity()
        glTranslate(-0.95, -0.1, 0.0)
        glScale(0.4, 0.4, 0.0)
        UP_side_trap()
        down_side_trap()

    def draw_side_trap_2():
        glLoadIdentity()
        glTranslate(-0.95, -0.2, 0.0)
        glScale(0.4, 0.4, 0.0)
        UP_side_trap()
        down_side_trap()

    def draw_side_trap_3():
        glLoadIdentity()
        glTranslate(-0.95, -0.3, 0.0)
        glScale(0.4, 0.4, 0.0)
        UP_side_trap()
        down_side_trap()

    def scene_2():
        glClearColor(0.2, 0.2, 0.2, 1)
        draw_left_wall()
        draw_Up_wall()
        draw_right_wall()
        draw_gound()
        draw_side_trap_1()
        draw_side_trap_2()
        draw_side_trap_3()
    scene_2()
    drawText("It's so easy",-.75,.7)
#scene
def S5():
    def walls(red,green,blue):
        glColor(red,green,blue)
        glBegin(GL_POLYGON)
        glVertex2d(-0.5,0.5)
        glVertex2d(0.5,0.5)
        glVertex2d(0.5,-0.5)
        glVertex2d(-0.5,-0.5)
        glEnd()

    def roof():
        glLoadIdentity()
        glScale(2,0.1,0.0)
        glTranslate(0.0,9.5,0.0)
        walls(0.7,0.7,0.7)

    def right_wall():
        glLoadIdentity()                  # remember el mafrod tmoot hna ,, ya 7ABAAAAAAAAAAAAAAAAAAAAL !!!!!
        glScale(0.3,1.5,0.0)
        glTranslate(2.82,-0.2,0)
        walls(0.7,0.7,0.7)

    def ground():
        glLoadIdentity()
        glScale(1.8,0.5,0.0)
        glTranslate(-0.1,-1.5,0.0)
        walls(0.7,0.7,0.7)

    def left_wall():
        glLoadIdentity()
        glScale(0.15,1,0.0)
        glTranslate(-4.5,0.5,0.0)
        walls(0.7,0.7,0.7)


    def scene():
        roof()
        right_wall()
        left_wall()
        ground()





        glLoadIdentity()
        glRotate(180,0,0,1)
        glScale(0.1,0.1,0)
        for x in range (0,-6,-1):
            triangle(x,4.5,1,1,1)    # the knifes lol
    scene()
    drawText("Try to die",-.6,.7)
#named abdo
def S6():
    glLoadIdentity()     #top
    glScale(2,0.2,0)
    square(0,5,0.7,0.7,0.7)

# left bottom corner
    glLoadIdentity()
    glTranslate(-0.9, -0.9, 0)
    glScale(0.823, 1.5, 0)
    square(0, 0, 0.7, 0.7, 0.7)

#elyamen
    glLoadIdentity()
    glTranslate(0.9,-0.9,0)
    glScale(1.18,1.5,0)
    square(0,0,.7,.7,.7)

#fe elnos elsoghair t7t khales
    glLoadIdentity()
    glTranslate(-0.09,-.95,0)
    glScale(.8,.13,0)
    square(0,0,.7,.7,.7)

#fel elnos elsoghair foq
    glLoadIdentity()
    glTranslate(-0.09,-0.215,0)
    glScale(.8,.13,0)
    square(0,0,0.7,0.7,0.7)

    glLoadIdentity()             # knifes
    glRotate(180, 0, 1, 0)
    glRotate(180,0,0,1)
    glScale(0.1,0.1,0)
    for x in range (3):
        triangle(x-5,1,1,1,1)
    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glRotate(180,0,0,1)
    glScale(0.1,0.1,0)
    for x in range (3):
        triangle(x,1,1,1,1)



    glLoadIdentity()
    glScale(0.09,0.6,0)
    square(-1.6,1.08,0.7,0.7,0.7) # over the DOOR



    glLoadIdentity()
    glTranslate(0.8,0.03,0)
    glScale(1,1.82,0)
    glColor(0.7,0.7,0.7)
    glBegin(GL_POLYGON)
    glVertex3d(0, 0.07, 0)
    glVertex3d(0, 0.2, 0)
    glVertex3d(0.2, 0.2, 0)
    glVertex3d(0.2, -0.1, 0)
    glVertex3d(-0.3, -0.1, 0)
    glVertex3d(-0.3, 0.07, 0)
    glEnd()                    # LADDER

    glLoadIdentity()
    glRotate(180,0,1,0)
    glTranslate(0.8,0.03,0)
    glScale(1,1.82,0)
    glColor(0.7,0.7,0.7)
    glBegin(GL_POLYGON)
    glVertex3d(0, 0.07, 0)
    glVertex3d(0, 0.229, 0)
    glVertex3d(0.2, 0.229, 0)
    glVertex3d(0.2, -0.1, 0)
    glVertex3d(-0.3, -0.1, 0)
    glVertex3d(-0.3, 0.07, 0)
    glEnd()
    drawText("Deadly ground",-.53,.7)
#named deep
def S7():
    def ladder(xs=.3, ys=.15, xT=0, yT=0):
        glLoadIdentity()
        glTranslate(xT, yT, 0)
        glScale(xs, ys, 0)
        square(0, 0, 0.7, 0.7, 0.7)


    def saw(Tx, Ty):
        glLoadIdentity()
        glTranslate(Tx, Ty, 0)
        glScale(.1, .1, 0)
        glBegin(GL_POLYGON)
        glColor(1, 1, 1)
        glVertex2d(0, -.5)
        glVertex2d(0, .5)
        glVertex2d(-.5, 0)
        glEnd()


    def saw_right(Tx, Ty):
        glLoadIdentity()
        glTranslate(Tx, Ty, 0)
        glScale(.1, .1, 0)
        glBegin(GL_POLYGON)
        glColor(1, 1, 1)
        glVertex2d(0, -.5)
        glVertex2d(0, .5)
        glVertex2d(.5, 0)
        glEnd()

    glLoadIdentity()
    glTranslate(0, -0.9, 0)
    glScale(2, 0.5, 0)
    square(0, 0, 0.7, 0.7, 0.7)  # THE GROUND

    glLoadIdentity()
    # glRotate(180, 0, 1, 0)
    glTranslate(0, 0.95, 0)
    glScale(2, 0.15, 0)
    square(0, 0, 0.7, 0.7, 0.7)  # TOP
    ladder(.15, 1.2, 0.7, 0.5)
    ladder(.3, .3, -.9, .25)
    ladder(.6, .3, -.8, 0)
    ladder(.9, .3, -.7, -.25)
    ladder(1.2, .3, -.6, -.5)

    # left_triangle
    glLoadIdentity()
    # glRotate(180, 0, 1, 0)
    glTranslate(1.3, -.7, 0)
    glScale(.3, .3, 0)
    glRotate(180, 0, 0, 1)
    triangle(.7, -.5, 0.7, 0.7, 0.7)

    # saws
    saw(.625, .2)
    saw(.625, .1)
    saw(.625, 0)
    saw_right(.775, .2)
    saw_right(.775, .1)
    saw_right(.775, .0)
    drawText("You're gonna fail us",-.75,.7)

