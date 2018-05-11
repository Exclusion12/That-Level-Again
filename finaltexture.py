from OpenGL.GL import *
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import pygame 

texture=[]
image=1
ix=0
iy=0



def texture_setup(image_name, texture_num, ix, iy):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBindTexture(GL_TEXTURE_2D, texture[texture_num])
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glEnable(GL_TEXTURE_2D)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE,image_name)




def LoadTextures(img):
    global image,ix,iy
    image=pygame.image.load(img)
    ix=image.get_width()
    iy=image.get_height()
    image=pygame.image.tostring(image,'RGB',1)
    global texture
    texture=glGenTextures(2)
    texture_setup(image,0, ix, iy)



def squaret():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor(1,1,1)
    glBegin(GL_QUADS)
    glTexCoord2f(0,0)
    glVertex3f(-1, -1, -.5)  # Bottom Left of The Texture and Quad
    glTexCoord2f(1,0)
    glVertex3f(1, -1, -.5)  # Bottom Right of The Texture and Quad
    glTexCoord2f(1,1)
    glVertex3f(1, 1, -.5)  # Top Right of The Texture and Quad
    glTexCoord2f(0,1)
    glVertex3f(-1,1 , -.5)# Top Left of The Texture and Quad
    glEnd()


def DrawT(img):
    LoadTextures(img)
    squaret()  # "0" is the first index no. of a six member sequence - images.
