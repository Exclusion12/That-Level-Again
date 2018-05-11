from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import pygame
from controllingFunc import *

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width,hight)
    glutCreateWindow(b'mygame')
    init()
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutKeyboardFunc(keyboard)
    glutKeyboardUpFunc(keyboardup)
    glutSpecialFunc(keyboards)
    glutMouseFunc(mouse)
    glutPassiveMotionFunc(mose)
    glutMainLoop()
main()
