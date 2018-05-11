from variables import *
import winsound
from finaltexture import *

def init():
    glClearColor(.2, .2, .2, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1,1,-1,1,-1,1)  # l,r,b,t,n,f
    glMatrixMode(GL_MODELVIEW)

### fucn to check the color if pixels in a row start from x,y and till the counter in right direction
def Xgenerate(x,y,counter,checker):
    xvar = []
    for i in range (counter) :
        xvar = (GLubyte *1)(0)
        glReadPixels(x+i,y,1,1,GL_RGB,GL_UNSIGNED_BYTE,xvar)
        if checker != xvar[0]:
            if xvar[0]==255:
                return "dead"
            if xvar[0]==178:
                return False
    return True

### fucn to check the color if pixels in a colomn start from x,y and till the counter in the up direction
def Ygenerate(x,y,counter,checker):
    yvar= []
    for i in range (counter) :
        yvar = (GLubyte *1)(0)
        glReadPixels(x,y+i,1,1,GL_RGB,GL_UNSIGNED_BYTE,yvar)
        if checker != yvar[0]:
            if yvar[0]==255:
                return "dead"
            if yvar[0]==178:
                return False
    return True

## to catch the key and drop it if mouse clicked
def mouse(button,state,x,y):
    global but,xi,yi,xm,ym,catch
    xm=x
    ym=y
    xm,ym=S_2_w(xm,ym)
    if state == GLUT_LEFT:
        if xm>xi-.02 and xm<xi+.12 and ym>yi-.02 and ym <yi+.02:
            if sound:
                winsound.PlaySound('sounds/crick.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_PURGE)
            catch=not catch
            but = not but
        else:
            but = False

### check if the character touches the key and make the character hold it
def collation_key():
    global xi,yi,xd,mov,catch,caught
    if catch:
        if (xi-.01<=xd+.03125 and xi-.01>=xd-.03125) or (xi+.07<=xd+.03125 and xi+.07>=xd-.03125 ) or (xi>=xd-.03125 and xi<=xd+.03125):
            if (yi+.01<=mov+.0625 and yi+.01>=mov-.0625) or (yi-.01<=mov+.0625 and yi-.01>=mov-.0625):
                xi=xd
                yi=mov
                caught=True
## to activate the moveing if the key is pressed
def keyboard(key,x,y):
    global keys,xd,i,started
    if key==b'p' and (started or paused):
        keys['p']=True
    if key==b'\x1b':
        keys["escape"]=True
    if key == b'\r':
        keys["enter"]=True
    if key ==b'w' and i!=2:
        keys['w']=True
    if key==b'd':
        keys['d']=True
    if key==b'a':
        keys['a']=True
    if key==b'f' and i==2:
        keys['f']=True
    if key==b'u' and i==1:
        keys['u']=True
    if key==b'j' and i==1:
        keys['j']=True
    if key == b'q':
        sys.exit()
def keyboards(key,x,y):
    global keys
    if key==GLUT_KEY_UP:
        keys["up"]=True
    elif key==GLUT_KEY_DOWN:
        keys["down"]=True
### to deactivate the moving if the key is not pressed
def keyboardup(key,x,y):
    global keys,angle
    if key==b'\x1b':
        keys["escape"]=False
    if key==b'd':
        keys['d']=False
        angle=0
    if key==b'a':
        keys['a']=False
        angle=0
    if key==b'f':
        keys['f']=False
    if key==b'u' :
        keys['u']=False
    if key==b'j':
        keys['j']=False
# convert from windows cordinates to secreen cordenate so that we can use mouse cordinate in the code
def S_2_w (x,y):
    global w,h
    if x > w:
        xa=(x-w)/w
    else:
        xa=-(w-x)/w
    if y > h :
        ya=-(y-h)/h
    else:
        ya=(h-y)/h
    alist=[xa,ya]
    return alist


# convert from windows cordinates to secreen cordenate so that we can use mouse cordinate in the code
def W_2_s (x,y):
    global width,hight
    xa=-1-x
    ya=1-y
    xa=ceil(abs(xa/2)*width)
    ya=ceil(abs(ya/2)*hight)
    alist=[xa,ya]
    return alist

## to move the key with the mouse if caught
def mose(x,y):
    global xn,yn
    xn=x
    yn=y

def reset():
    global xi,yi,xn,yn,but,xp,yp,vbasic,v_velocity,xmov,mov,xd,ju,again,swapedup,swapedl,swapedr,paused
    global keyi,i,keys,catch,caught,xm,ym,ironman,upsc2,door,angle,started,xc,yc,p,options ,credits,sound
    xi=.85 # key x translation
    yi=-.15 # key y translation
    xn=0
    yn=0
    but = False # key caught check
    xp=0
    yp=0
    vbasic=2.9
    v_velocity = vbasic # Vertical Velocity of the ball
    xmov=.005*1.5 # x speed for the player
    mov=0 # player y translation
    xd=0 # player x translation
    ju=False ## to know if he is jumping or not
    again=True ## to prevent character from double jumping
    swapedr=False
    swapedl=False
    swapedup=False
    i=0
    keyi=i
    keys={'w':False,'d':False,'a':False,'f':False,'u':False,'j':False,"up":False,"down":False,"enter":False,"escape":False,'p':False}
    catch=True ## to check if the key is catched or not
    caught=False
    xm=0
    ym=0
    ironman=False
    upsc2=0
    door=[False,False,False,False,False,False,False]
    angle=0
    started=False
    xc=0
    yc=0
    p=1
    options=True
    credits=False
    sound=True
    paused=False

def draw():
    global dtime,v_velocity,ar,data,xmov,i,vbasic,h,w,upsc2,angle,xc,yc,started,options,credits,sound
    global p,keys,mov,xd,ju,again,swapedr,swapedl,swapedup,door
    global xn,yn,but,yi,xi,keyi,caught,xm,ym,paused,fin
    glDisable(GL_TEXTURE_2D)
    glClear(GL_COLOR_BUFFER_BIT)
    global width,hight
    m=(GLuint *4)(0)
    glGetIntegerv(GL_VIEWPORT,m)
    width,hight=m[2],m[3]
    w,h=width//2,hight//2
    ratiow=width/600
    ratioh=hight/600
    if started:
        if keys['p']:
            paused=True
            keys['p']=False
            started=False
        s2x,s2y=S_2_w(xn,yn)
        if but==True:
            xi=s2x
            yi=s2y

        ### swapping between scenes if the character passed through the screen
        if xd > .99-.03125:
            i+=1
            swapedr=True
        elif xd < -.99+.03125:
            i-=1
            swapedl=True
        if mov>.99-.0625 and i==2:
            i+=1
            swapedup=True
        if swapedr:
            if caught:
                xd=-.99+.03125
                xi=xd
                keyi=i
            else:
                xd=-.99+.03125
            swapedr =False
        elif swapedl:
            if caught:
                xd=.99-.03125
                xi=xd
                keyi=i
            else:
                xd=.99-.03125
            swapedl =False
        elif swapedup:
            if caught:
                mov=-.99+.0625
                yi=mov
                keyi=i
            else:
                mov=.99+.0625
            swapedup =False

        if not (xd>xi-.01 and xd<xi+.07 and mov>yi-.01 and mov <yi+.01):
            caught=False
        else:
            caught=True
        if i!=7:
            ar[i]()
        else:
            started=False
            fin=True
        if i!=7:
            if yi>=-.24 and yi<=.35 and xi+.07>=.07 and caught and i==2 :
                door[i]=True
            if door[i] and i==2:
                glLoadIdentity()
                glScale(0.1,0.6,0)
                square(1.2,0.1,0.2,.2,1) # DOOR
            elif i==2:
                glLoadIdentity()
                glScale(0.1,0.6,0)
                square(1.2,0.1,0.7,0.2,1) # DOOR

            if yi>=-.5 and yi<=0 and xi+.07>=-.676 and caught and i==4 :
                door[i]=True
            if door[i] and i==4:
                glLoadIdentity()
                glScale(0.05,0.5,0)
                square(-13,-0.5,0.2,0.2,1) # DOOR
            elif i==4:
                glLoadIdentity()
                glScale(0.05,0.5,0)
                square(-13,-0.5,0.7,0.2,1) # DOOR

            if yi>=-.15 and yi<=.35 and xi+.07>=-.18 and caught and i==5 :
                door[i]=True
            if door[i] and i==5:
                glLoadIdentity()
                glScale(0.07,0.5,0)
                square(-2,0.2,0.2,0.2,1) # DOOR
            elif i==5:
                glLoadIdentity()
                glScale(0.07,0.5,0)
                square(-2,0.2,0.7,0.2,1) # DOOR

            if yi>=-.648 and yi<=-.1 and xi+.07>=.7 and caught and i==6 :
                door[i]=True
            if door[i] and i==6:
                glLoadIdentity()
                glScale(0.07, 0.55, 0)
                square(10.5, -0.68, 0.2, 0.2, 1)  # DOOR
            elif i==6:
                glLoadIdentity()
                glScale(0.07, 0.55, 0)
                square(10.5, -0.68, 0.7, 0.2, 1)  # DOOR
            a,b=W_2_s(xd-.03125,-(mov+.0625))
            topchecker = Xgenerate(a+2,b+2,ceil(15*ratiow),51)

            if i==1:
                if keys['u'] and topchecker:
                    upsc2+=xmov
                    if (xd-.03125>=-.73 and xd-.03125<=-.41 and mov-.0625<=upsc2+.04 and mov-.0625>=upsc2-.04)or(xd+.03125>=-.73 and xd+.03125<=-.41 and mov-.0625<=upsc2+.04 and mov-.0625>=upsc2-.04):
                        mov+=xmov
                if keys['j'] :
                    upsc2-=xmov
                    if (xd-.03125>=-.73 and xd-.03125<=-.41 and mov-.0625<=upsc2+.04 and mov-.0625>=upsc2-.04)or(xd+.03125>=-.73 and xd+.03125<=-.41 and mov-.0625<=upsc2+.04 and mov-.0625>=upsc2-.04):
                        mov-=xmov

                glLoadIdentity()
                glColor(.7,.7,.7)
                glTranslate(0,upsc2,0)
                glBegin(GL_POLYGON)
                glVertex(-.73,.08)
                glVertex(-.73,0)
                glVertex(-.41,0)
                glVertex(-.41,.08)
                glEnd()
                 # moving pad scene2
            ### collision detection defenition
            ## the width of the character in pixels is 17 and its hight is 38
            a,b=W_2_s(xd-.03125,-(mov+.0625))
            topchecker = Xgenerate(a+2,b+2,ceil(15*ratiow),51)
            a,b=W_2_s(xd-.03125,-(mov-.0625))
            bottomchecker = Xgenerate(a+2,b-2,ceil(15*ratiow),51)

            a,b=W_2_s(xd-.03125,-(mov-.0625))
            leftchecker = Ygenerate(a-2,b+2,ceil(35*ratioh),51)

            a,b=W_2_s(xd+.03125,-(mov-.0625))
            rightchecker = Ygenerate(a,b+2,ceil(35*ratioh),51)
            ### collision detection
            if rightchecker=="dead" or leftchecker=="dead" or topchecker=="dead" or bottomchecker=="dead":
                if sound:
                    winsound.PlaySound('sounds/ayyy.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_PURGE)
                if i==4:
                    xd=.7
                    mov=.7
                elif i==2 or i==1 or i== 5:
                    xd=-.5
                    mov=.5
                else:
                    xd=.5
                    mov=.5
            ### moving the characer
            if keys['w'] and again and bottomchecker==False:
                ju=True
                again=False
                if sound:
                    winsound.PlaySound('sounds/heq.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_PURGE)
            if keys['d'] and rightchecker==True:
                xd+=xmov
                angle=45
            if keys['a'] and leftchecker==True:
                xd-= xmov
                angle=-45
            if keys['f'] and topchecker==True:
                mov+=xmov
            ### jumping equations
            if ju :
                v_velocity = v_velocity - 9.8 * dtime
                mov = mov + v_velocity * dtime
                if v_velocity <= 0 or topchecker!=True :    # el collision el fo2 hyb2a be or m3a el shrt da (el pixels el fo2 mesh hya el background) kos om 7yaty
                    ju=False
            a,b=W_2_s(xd-.03125,-(mov-.0625))
            bottomchecker = Xgenerate(a+2,b-2,ceil(15*ratiow),51)
            if keys['f'] and topchecker==True:
                mov+=xmov
                bottomchecker=False
            if (bottomchecker==True) and not ju:
                v_velocity = v_velocity + 9.8 * dtime
                mov = mov - v_velocity * dtime
            elif bottomchecker!=True :
                again = True
                v_velocity=vbasic
                keys['w']=False
            glLoadIdentity()
            collation_key()
            if caught or keyi==i:
                glTranslate(xi, yi, 0)
                objectk()
            if i==0:

                glColor(.6,0,0)
                glLineWidth(3)
                glBegin(GL_LINE_STRIP)
                for j in np.arange(0,2*pi,.01):
                    xr=.83+.08*cos(j)
                    yr=.7+.04*sin(j)
                    glVertex(xr,yr)
                glEnd()

                glTranslate(.8,.7,0)
                glScale(1.5,1.5,1)
                objectk()
            glLoadIdentity()
            glTranslate(xd, mov, 0)
            glRotate(angle,0,1,0)
            object()
    elif options:
        DrawT(b"designs/optioninternal.png")
        if keys["up"]:
            if p==1:
                p=2
            else:
                p=1
            keys["up"]=False
        elif keys["down"]:
            if p==2:
                p=1
            else:
                p=2
            keys["down"]=False
        if p==1:
            xc=-.3
            yc=.4
        elif p==2:
            xc=-0.3
            yc=-0.2
        glColor(0,1,0)
        glScale(1.2,1.2,1)
        glTranslate(xc,yc,0)
        glBegin(GL_POLYGON)
        glVertex(0,0,.5)
        glVertex(-.1,.1,.5)
        glVertex(-.1,-.1,.5)
        glEnd()
        if keys["enter"]:
            if p==1:
                reset()
            elif p==2:
                sound=not sound
            keys["enter"]=False
        if keys["escape"]:
            options=False
            keys["escape"]=False
            p=1
    elif fin:
        DrawT(b"designs/dexter.png")
    elif credits:
        DrawT(b"designs/aboutus.png")
        if keys["escape"]:
            credits=False
            keys["escape"]=False
            p=1
    elif paused:
        DrawT(b"designs/pause.png")
        if keys['p']:
            started=True
            paused=False
            keys['p']=False
        if keys["escape"]:
            paused=False
            p=1
    else:
        DrawT(b"designs/Startpage.png")
        if keys["up"]:
            if p==1:
                p=3
            else:
                p-=1
            keys["up"]=False
        elif keys["down"]:
            if p==3:
                p=1
            else:
                p+=1
            keys["down"]=False
        if p==1:
            xc=-.25
            yc=.455
        elif p==2:
            xc=-.25
            yc=.055
        elif p==3:
            xc=.8
            yc=-.85
        glColor(0,1,0)
        glTranslate(xc,yc,0)
        glBegin(GL_POLYGON)
        glVertex(0,0,.5)
        glVertex(-.1,.1,.5)
        glVertex(-.1,-.1,.5)
        glEnd()
        if keys["enter"] and p==1:
            started=True
            options=False
            credits=False
            keys["enter"]=False
        elif keys["enter"] and p==2:
            options=True
            started=False
            credits=False
            keys["enter"]=False
            p=1
        elif keys["enter"] and p==3:
            credits=True
            started=False
            options=False
            keys["enter"]=False
            p=1

    glFlush()
### drawing the character
def object():

#neck
    glScale(.1451612903225806,.1357142857142857,1)
    glColor(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(.05,.06)
    glVertex2d(-.05,.06)
    glVertex2d(-.035,.08)
    glVertex2d(.035,.08)
    glEnd()

    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(.05,.06)
    glVertex2d(-.05,.06)
    glVertex2d(-.035,.08)
    glVertex2d(.035,.08)
    glEnd()

#right leg
    glColor(1,.82,0)
    glBegin(GL_POLYGON)
    glVertex2d(.1,-.4)
    glVertex2d(.01,-.4)
    glVertex2d(.01,-.21)
    glVertex2d(.1,-.21)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(.1,-.4)
    glVertex2d(.01,-.4)
    glVertex2d(.01,-.21)
    glVertex2d(.1,-.21)
    glEnd()
#left leg
    glColor(1,.82,0)
    glBegin(GL_POLYGON)
    glVertex2d(-.1,-.4)
    glVertex2d(-.01,-.4)
    glVertex2d(-.01,-.21)
    glVertex2d(-.1,-.21)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(-.1,-.4)
    glVertex2d(-.01,-.4)
    glVertex2d(-.01,-.21)
    glVertex2d(-.1,-.21)
    glEnd()
#pants
    glColor(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(.09,-.15)
    glVertex2d(.1,-.205)
    glVertex2d(0,-.26)
    glVertex2d(-.1,-.205)
    glVertex2d(-.09,-.15)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(.09,-.15)
    glVertex2d(.1,-.205)
    glVertex2d(0,-.26)
    glVertex2d(-.1,-.205)
    glVertex2d(-.09,-.15)
    glEnd()
#right shoe
    glColor(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(.1,-.35)
    glVertex2d(.102,-.45)
    glVertex2d(.01,-.45)
    glVertex2d(.01,-.35)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(.15,-.45)
    glVertex2d(.102,-.45)
    glVertex2d(.1,-.4)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(.1,-.35)
    glVertex2d(.1,-.4)
    glVertex2d(.15,-.45)
    glVertex2d(.01,-.45)
    glVertex2d(.01,-.35)
    glEnd()
    glColor(1,.82,0)
    glBegin(GL_POLYGON)
    glVertex2d(.01,-.35)
    for i in np.arange(0,-.5*pi,-.01):
        x=.04*cos(i)
        y=.04*sin(i)
        glVertex2d(x+.01,y-.35)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_POINTS)
    for i in np.arange(0,-.5*pi,-.09):
        x=.04*cos(i)
        y=.04*sin(i)
        glVertex2d(x+.01,y-.35)
    glEnd()


#left shoe
    glColor(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(-.1,-.35)
    glVertex2d(-.102,-.45)
    glVertex2d(-.01,-.45)
    glVertex2d(-.01,-.35)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(-.15,-.45)
    glVertex2d(-.102,-.45)
    glVertex2d(-.1,-.4)
    glEnd()
    glColor(1,.82,0)
    glBegin(GL_POLYGON)
    glVertex2d(-.01,-.35)
    for i in np.arange(pi,1.5*pi,.01):
        x=.04*cos(i)
        y=.04*sin(i)
        glVertex2d(x-.01,y-.35)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_POINTS)
    for i in np.arange(pi,1.5*pi,.09):
        x=.04*cos(i)
        y=.04*sin(i)
        glVertex2d(x-.01,y-.35)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(-.1,-.35)
    glVertex2d(-.1,-.4)
    glVertex2d(-.15,-.45)
    glVertex2d(-.01,-.45)
    glVertex2d(-.01,-.35)
    glEnd()

#face
    glColor(1,0,0)
    glBegin(GL_POLYGON)
    for i in np.arange(0,2*pi,.01):
        x=.2*cos(i)
        y=.2*sin(i)
        glVertex2d(x,y+.28)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    for i in np.arange(0,2*pi,.01):
        x=.2*cos(i)
        y=.2*sin(i)
        glVertex2d(x,y+.28)
    glEnd()
#mask
    glColor(1,.82,0)
    glBegin(GL_POLYGON)
    glVertex2d(0,.35)
    glVertex2d(0.09,.35)
    glVertex2d(0.04,.15)
    glVertex2d(0,.15)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(0,.35)
    glVertex2d(-0.09,.35)
    glVertex2d(-0.04,.15)
    glVertex2d(0,.15)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2d(-0.09,.35)
    glVertex2d(-.11,.4)
    glVertex2d(-.203,.3)
    glVertex2d(-.11,.17)
    glVertex2d(-.06,.13)
    glVertex2d(-0.04,.15)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(0.09,.35)
    glVertex2d(.11,.4)
    glVertex2d(.203,.3)
    glVertex2d(.11,.17)
    glVertex2d(.06,.13)
    glVertex2d(0.04,.15)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(0.04,.15)
    glVertex2d(.06,.13)
    glVertex2d(-.06,.13)
    glVertex2d(-0.04,.15)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(0.09,.35)
    glVertex2d(.11,.4)
    glVertex2d(.203,.3)
    glVertex2d(.11,.17)
    glVertex2d(.06,.13)
    glVertex2d(0.04,.15)
    glVertex2d(-0.04,.15)
    glVertex2d(-.06,.13)
    glVertex2d(-.11,.17)
    glVertex2d(-.203,.3)
    glVertex2d(-.11,.4)
    glVertex2d(-0.09,.35)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex2d(.06,.13)
    glVertex2d(-.06,.13)
    glEnd()
#right eye
    glColor(.52156,.98431,.96078)
    glBegin(GL_POLYGON)
    glVertex2d(.1,.3)
    glVertex2d(.11,.275)
    glVertex2d(.05,.25)
    glVertex2d(.04,.28)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(.1,.3)
    glVertex2d(.11,.275)
    glVertex2d(.05,.25)
    glVertex2d(.04,.28)
    glEnd()
#left eye
    glColor(.52156,.98431,.96078)
    glBegin(GL_POLYGON)
    glVertex2d(-.1,.3)
    glVertex2d(-.11,.275)
    glVertex2d(-.05,.25)
    glVertex2d(-.04,.28)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(-.1,.3)
    glVertex2d(-.11,.275)
    glVertex2d(-.05,.25)
    glVertex2d(-.04,.28)
    glEnd()

#body
    glColor(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(.09,-.15)
    glVertex2d(.09,.06)
    glVertex2d(-.09,.06)
    glVertex2d(-.09,-.15)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(.09,-.15)
    glVertex2d(.09,.06)
    glVertex2d(-.09,.06)
    glVertex2d(-.09,-.15)
    glEnd()
#power source
    glColor(.52156,.98431,.96078)
    glBegin(GL_POLYGON)
    glVertex2d(0,-.03)
    glVertex2d(-.025,0.01)
    glVertex2d(.025,0.01)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(0,-.03)
    glVertex2d(-.025,0.01)
    glVertex2d(.025,0.01)
    glEnd()

#right sholder
    glColor(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(.09,0)
    for i in np.arange(.25*pi,.5*pi,.01):
        x=.06*cos(i)
        y=.06*sin(i)
        glVertex2d(x+.09,y)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(.09,0)
    for i in np.arange(.25*pi,.5*pi,.01):
        x=.06*cos(i)
        y=.06*sin(i)
        glVertex2d(x+.09,y)
    glEnd()

#left sholder
    glColor(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(-.09,0)
    for i in np.arange(.5*pi,.75*pi,.01):
        x=.06*cos(i)
        y=.06*sin(i)
        glVertex2d(x-.09,y)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(-.09,0)
    for i in np.arange(.5*pi,.75*pi,.01):
        x=.06*cos(i)
        y=.06*sin(i)
        glVertex2d(x-.09,y)
    glEnd()

#right arm
    glColor(1,.82,0)
    glBegin(GL_POLYGON)
    glVertex2d(.06*cos(.25*pi)+.09,.06*sin(.25*pi))
    glVertex2d(.09,0)
    glVertex2d(.11,-.18)
    glVertex2d(.06*cos(.25*pi)+.16,-.18)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(.06*cos(.25*pi)+.09,.06*sin(.25*pi))
    glVertex2d(.09,0)
    glVertex2d(.11,-.18)
    glVertex2d(.06*cos(.25*pi)+.16,-.18)
    glEnd()

#left arm
    glColor(1,.82,0)
    glBegin(GL_POLYGON)
    glVertex2d(-.06*cos(.25*pi)-.09,.06*sin(.25*pi))
    glVertex2d(-.09,0)
    glVertex2d(-.11,-.18)
    glVertex2d(-.06*cos(.25*pi)-.16,-.18)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(-.06*cos(.25*pi)-.09,.06*sin(.25*pi))
    glVertex2d(-.09,0)
    glVertex2d(-.11,-.18)
    glVertex2d(-.06*cos(.25*pi)-.16,-.18)
    glEnd()

#right hand
    glColor(1,0,0)
    glBegin(GL_POLYGON)
    for i in np.arange(pi,2*pi,.01):
        x=.035*cos(i)
        y=.035*sin(i)
        glVertex2d(x+.155,y-.18)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    for i in np.arange(pi,2*pi,.01):
        x=.035*cos(i)
        y=.035*sin(i)
        glVertex2d(x+.155,y-.18)
    glEnd()

#left hand
    glColor(1,0,0)
    glBegin(GL_POLYGON)
    for i in np.arange(pi,2*pi,.01):
        x=.035*cos(i)
        y=.035*sin(i)
        glVertex2d(x-.155,y-.18)
    glEnd()
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    for i in np.arange(pi,2*pi,.01):
        x=.035*cos(i)
        y=.035*sin(i)
        glVertex2d(x-.155,y-.18)
    glEnd()

    glLoadIdentity()

### drawing the key
def objectk ():
    glColor(.9019607843137255,1,.244)
    glScale(.01,.01,.01)
    glutSolidTorus(.5,1,20,30)
    glTranslate(.5,0,0)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex(0,0,0)
    glVertex(6,0,0)
    glEnd()
    for i in range (4):
        glBegin(GL_LINES)
        glVertex(5.9-(i*.5), 0, 0)
        glVertex(5.9-(i*.5), -1, 0)
        glEnd()
    glLoadIdentity()
